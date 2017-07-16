#!/usr/bin/env python

from __future__ import (
    absolute_import, division, print_function, unicode_literals)
from future.builtins import str, zip

import sys


def rot1(input_handle, output_file_name):
    open(output_file_name, 'w').write(
        ''.join(map(lambda x: chr(ord(x) + 1), input_handle.read())))


def rot2(input_file_name, output_file_name):
    open(output_file_name, 'w').write(
        ''.join(map(lambda x: chr(ord(x) + 2), open(input_file_name).read())))


def main():
    rot1(open(sys.argv[1]), sys.argv[2])


if __name__ == '__main__':
    main()
