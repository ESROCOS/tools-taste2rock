# H2020 ESROCOS Project
# Company: GMV Aerospace & Defence S.A.U.
# Licence: GPLv2


import os
import sys
import re
import subprocess

panicEnabled = True

def panic(x):
    '''Function called to abort with a message'''
    if not x.endswith("\n"):
        x += "\n"

    if sys.stderr.isatty():
        # Colour output
        x = chr(27) + "[31m" + x + chr(27) + "[0m"

    sys.stderr.write(x)

    if panicEnabled:
        # If disabled, don't exit (for debugging)
        sys.exit(1)


def banner(msg):
    '''Splashes message in big green letters'''
    if sys.stdout.isatty():
        print("\n", chr(27), "[32m", msg, chr(27), "[0m")
    else:
        print("\n", msg)
    sys.stdout.flush()


def print_error(msg):
    '''Splashes message in red letters'''
    if sys.stderr.isatty():
        msg = chr(27) + "[31m" + msg + chr(27) + "[0m"
    sys.stderr.write(msg)
    sys.stderr.flush()


def runInDir(dir, cmd):
    '''Runs a shell command in a given directory, and returns to the previous one'''
    if not os.path.isdir(dir):
        panic('Wrong directory {}.'.format(dir))
    old = os.getcwd()
    result = 0
    try:
        os.chdir(dir)
        result = subprocess.call(cmd)
    finally:
        os.chdir(old)
    return result


def replaceInFile(file, regex, subst):
    '''Replaces a regular expression in a file'''
    with open(file) as fd:
        contents = fd.read()
    contents = re.sub(regex, subst, contents)
    with open(file, 'w') as fd:
        fd.write(contents)
    



