import json
import yaml
from gendiff.parser import find_diff
from .formatter.formatter import formatter, FORMAT_STYLISH


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
