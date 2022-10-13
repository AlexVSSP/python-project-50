#!/usr/bin/python3
import argparse
from gendiff import generate_diff
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.json import json


def main():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Compares two configuration '
                                                 'files and shows '
                                                 'a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format",
                        help="set format of output", default="stylish")
    args = parser.parse_args()

    if args.format == "plain":
        print(generate_diff(args.first_file, args.second_file, plain))
    elif args.format == "json":
        print(generate_diff(args.first_file, args.second_file, json))
    else:
        print(generate_diff(args.first_file, args.second_file, stylish))


if __name__ == '__main__':
    main()
