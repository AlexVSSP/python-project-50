import json
import yaml
from .parser_module import parse
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain


def get_data(path_to_file):
    if path_to_file.endswith('json'):
        with open(path_to_file) as json.file:
            data = json.load(json.file)
        return data
    else:
        with open(path_to_file) as yaml.file:
            data = yaml.safe_load(yaml.file)
        return data


def generate_diff(input_file1, input_file2, format=stylish):
    diff = parse(get_data(input_file1), get_data(input_file2))
    if format == stylish:
        format_diff = stylish(diff)
        return format_diff
    elif format == plain:
        format_diff = plain(diff)
        return format_diff
