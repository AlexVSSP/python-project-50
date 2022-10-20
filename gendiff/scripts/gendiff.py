#!/usr/bin/python3
import argparse
from gendiff import generate_diff
from gendiff import FORMAT_STYLISH


def main():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Compares two configuration '
                                                 'files and shows '
                                                 'a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format",
                        help="set format of output", default=FORMAT_STYLISH)
    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
