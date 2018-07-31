#!/usr/bin/env python3

# H2020 ESROCOS Project
# Company: GMV Aerospace & Defence S.A.U.
# Licence: GPLv2

import sys, os, getopt, errno
from taste2rock import exporter, utilities


def main():
    try:
        if not exporter.check_rock_env_loaded():
            utilities.panic('Rock environment not loaded. Source env.sh.')
        
        binary_c, pkg_name = parse_args()
        exporter.export_rock_package(binary_c, pkg_name)
    except Exception as ex:
        utilities.panic('An exception occurred: {}'.format(ex))


def parse_args():
    '''
    Parse command-line arguments
    '''
    inputfile = ''
    outdir_asn = ''
    try:
        args = sys.argv[1:]
        optlist, args = getopt.gnu_getopt(
            args,
            'h',
            ['help'])
    except:
        usage()
        sys.exit(errno.EINVAL)
    
    for opt, arg in optlist:
        if opt == '-h':
            usage()
            sys.exit(0)

    if len(args) == 2:
        binary_c = args[0]
        out_dir = args[1]
    else:
        usage()
        sys.exit(errno.EINVAL)

    return binary_c, out_dir


def usage():
    '''
    Print command-line usage
    '''
    print('Usage: ' + os.path.basename(sys.argv[0]) + ' <taste_binary_dir> <rock_package_name>')


if __name__ == "__main__":
    main()
