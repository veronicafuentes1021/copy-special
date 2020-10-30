# give credits
__author__ = "Veronica Fuentes"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    result = []
    paths = os.listdir(dirname)
    for fname in paths:
        match = re.search(r'__(\w+)__', fname)
        if match:
            result.append(os.path.abspath(os.path.join(dirname, fname)))
    return result


def copy_to(path_list, dest_dir):
    """Given a list of paths and a dirname, copies special files."""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for path in path_list:
        fname = os.path.basename(path)
        shutil.copy(path, os.path.join(dest_dir, fname))


def zip_to(path_list, dest_zip):
    """Given a list of paths and a dirname, zips special files."""
    cmd = 'zip -j ' + dest_zip + ' ' + ' '.join(path_list)
    print('Command:' + cmd)
    (status, output) = subprocess.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)
        sys.exit(1)
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)
    path_list = get_special_paths(ns.from_dir)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    if ns.todir:
        copy_to(path_list, ns.todir)
    elif ns.tozip:
        zip_to(path_list, ns.tozip)
    for path in path_list:
        print(path)
    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])
