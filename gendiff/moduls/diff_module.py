import json
import yaml
from .parser_module import find_diff
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.json import json_ as json_format


FORMAT_STYLISH = 'stylish'
FORMAT_PLAIN = 'plain'
FORMAT_JSON = 'json'


def get_data(path_to_data):
    if path_to_data.endswith('json'):
        data = open(path_to_data).read()
        data_format = json
    elif path_to_data.endswith('yml') or path_to_data.endswith('yaml'):
        data = open(path_to_data)
        data_format = yaml
    else:
        raise Exception('Invalid data format specified!')
    return data, data_format


def parse_to_dict(data, data_format):
    if data_format == json:
        data_to_parse = data_format.loads(data)
    else:
        data_to_parse = data_format.safe_load(data)
    return data_to_parse


def generate_diff(input_data1, input_data2, format_=FORMAT_STYLISH):
    data1, data1_format = get_data(input_data1)
    data2, data2_format = get_data(input_data2)
    diff = find_diff(parse_to_dict(data1, data1_format),
                     parse_to_dict(data2, data2_format))
    return formatter(format_, diff)


def formatter(format_, diff):
    if format_ == FORMAT_STYLISH:
        format_diff = stylish(diff)
        return format_diff
    elif format_ == FORMAT_PLAIN:
        format_diff = plain(diff)
        return format_diff
    elif format_ == FORMAT_JSON:
        format_diff = json_format(diff)
        return format_diff
