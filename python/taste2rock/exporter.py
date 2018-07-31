# H2020 ESROCOS Project
# Company: GMV Aerospace & Defence S.A.U.
# Licence: GPLv2


import os, sys, shutil, glob, subprocess
from mako.template import Template

from .utilities import panic, runInDir, replaceInFile, print_error
from .IvData import IvData
from .IvDataRockMixin import IvDataRockMixin

# Mako templates
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
COMPONENT_OROGEN = Template(filename=(TEMPLATE_DIR + os.sep + 'component.orogen.mako'))
START_RB = Template(filename=(TEMPLATE_DIR + os.sep + 'start.rb.mako'))



# Mixin class for IvData
class IvDataRock(IvDataRockMixin, IvData):
    pass


def export_rock_package(binary_c, pkg_name):
    '''
    Main function to export a rock package from a TASTE model.
    Receives the binary folder of the TASTE model (normally, binary.c),
    and the name of the ROCK package to generate, which is also used 
    to build the output directory name.
    '''
    create_output_dir(pkg_name)
    iv = load_iv(binary_c)
    export_all_functions(iv, pkg_name)
    


def create_output_dir(pkg_name):
    '''Create an output directory for the ROCK package'''
    if not os.path.exists(pkg_name):
        os.makedirs(pkg_name)


def create_orogen(rock_pkg):
    '''
    Invoke rock-create-orogen to interactively initialize a package.
    '''
    result = subprocess.call(['rock-create-orogen', rock_pkg])
    if 0 != result:
        panic('Couldn\'t create Rock package ' + rock_pkg + '; rock-create-orogen failed')
    

def load_iv(binary_c):
    '''Loads the iv.py file'''
    # Check and load the input files from TASTE
    if not os.path.isdir(binary_c):
        panic('Cannot load the Interface View data: ' + binary_c + ' not found.')

    iv_path = os.sep.join([binary_c, 'iv.py'])
    if not os.path.isfile(iv_path):
        panic('Cannot load the Interface View data: ' + iv_path + ' not found.')

    return IvDataRock(iv_path)


def export_all_functions(the_iv, pkg_name):
    '''Export all TASTE functions in an Interface View and create start script'''
    for fun in the_iv.list_functions():
        fdir = create_function_component(the_iv, fun.lower(), pkg_name)

    print('')
    print('Orogen files have been created for the TASTE functions.')
    print('Generate ROCK task skeletons? [Y/n]')
    answer = sys.stdin.read(1).strip().lower()
    if len(answer) == 0 or answer == 'y':
        for fun in the_iv.list_functions():
            generate_task(pkg_name, fun)

    # Generate a start script
    gen_start_script(the_iv, os.path.join(pkg_name, 'start.rb'))


def create_function_component(the_iv, name, pkg_name):
    ''' Creates a Rock component for a TASTE function'''
    orogen_txt = COMPONENT_OROGEN.render(iv=the_iv, package=pkg_name, function=name)
    create_rock_component(name, orogen_txt, pkg_name)


def create_rock_component(name, orogen_txt, base_dir):
    ''' Creates a Rock component using a given Orogen file'''
    # Initialize orogen component
    print('==========================================')
    print('Creating Orogen component for the TASTE function {}. Enter data for {}.'.format(name, name))
    result = runInDir(base_dir, ['rock-create-orogen', name])
    if result != 0:
        print('ERROR running rock-create-orogen to initialize {} Rock component.'.format(name))
    else:
        # Write the .orogen file
        with open(os.path.join(base_dir, name, name + '.orogen'), 'w') as fd:
            fd.write(orogen_txt)


def generate_task(pkg_name, function):
    '''Invoke Rock to generate the task implementation from an orogen.'''
    result = runInDir(os.path.join(pkg_name, function), 'rock-create-orogen')
    if result != 0 or not os.path.exists(os.path.join(pkg_name, function, 'tasks', function+'Task.cpp')):
        print('ERROR running rock-create-orogen to generate {} Rock task.'.format(function))


def check_rock_env_loaded():
    '''Checks if the env.sh file for the Rock installation has been loaded'''
    return None != os.getenv('AUTOPROJ_CURRENT_ROOT')


def gen_start_script(the_iv, out_file='start.rb'):
    '''Generates the Rock start script for a system exported from TASTE'''
    script = START_RB.render(iv=the_iv)
    with open(out_file, 'w') as fd:
        fd.write(script)


