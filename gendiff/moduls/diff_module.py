import json
import yaml
from .parser_module import parse
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.json import json as json_format


FORMAT_STYLISH = 'stylish'
FORMAT_PLAIN = 'plain'
FORMAT_JSON = 'json'


def get_data(path_to_file):
    if path_to_file.endswith('json'):
        data = open(path_to_file).read()
        data_format = json
    elif path_to_file.endswith('yml') or path_to_file.endswith('yaml'):
        data = open(path_to_file)
        data_format = yaml
    else:
        raise Exception('Invalid data format specified!')
    return data, data_format


def get_parser(data, data_format):
    if data_format == json:
        data_to_parse = data_format.loads(data)
    else:
        data_to_parse = data_format.safe_load(data)
    return data_to_parse


def generate_diff(input_file1, input_file2, format=FORMAT_STYLISH):
    data1, data1_format = get_data(input_file1)
    data2, data2_format = get_data(input_file2)
    diff = parse(get_parser(data1, data1_format),
                 get_parser(data2, data2_format))
    return formatter(format, diff)


def formatter(format, diff):
    if format == FORMAT_STYLISH:
        format_diff = stylish(diff)
        return format_diff
    elif format == FORMAT_PLAIN:
        format_diff = plain(diff)
        return format_diff
    elif format == FORMAT_JSON:
        format_diff = json_format(diff)
        return format_diff
