#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import argparse

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def collect_paths(dir):
    file_dir = os.listdir(dir)
    match_file = [os.path.abspath(file) for file in file_dir if re.search(r'__\w+__', file)]

    return match_file


def copy_files(path_list, to_dir):
    if os.path.exists(to_dir):
        


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='positional argument defined by user input')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()

    print args.from_dir

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.
    paths = collect_paths(args.from_dir)

    if not paths:
        print 'No bueno'
    elif paths and args.todir:
        copy_files(paths, args.todir)


    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions
  
if __name__ == "__main__":
    main()
