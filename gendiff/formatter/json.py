import itertools
import re


def sort_by_second_part_of_key(item):
    key, value = item
    sign, word = key.split(' ', maxsplit=1)
    return str(word.strip())


def check_exceptions(element):
    if element is True:
        return "true"
    if element is False:
        return "false"
    if element is None:
        return "null"
    if isinstance(element, int):
        return element
    return f'"{element}"'


def nested_check(indict):
    if not isinstance(indict, dict):
        return indict
    else:
        dictionary = {}
        for k, v in indict.items():
            dictionary[f'  {k}'] = nested_check(v)
    return dictionary


# flake8: noqa: C901
def add_sign(dictionary):
    new_dict = {}
    for key, val in dictionary.items():
        if val['type'] == 'deleted':
            new_dict[f'- {key}'] = nested_check(val['value'])
        elif val['type'] == 'added':
            new_dict[f'+ {key}'] = nested_check(val['value'])
        elif val['type'] == 'unchanged':
            new_dict[f'  {key}'] = nested_check(val['value'])
        elif val['type'] == 'changed':
            new_dict[f'- {key}'] = nested_check(val['from'])
            new_dict[f'+ {key}'] = nested_check(val['to'])
        elif val['type'] == 'nested':
            new_dict[f'  {key}'] = add_sign(val['value'])
    return new_dict


def sorted_json(item_to_sort):
    sorted_item = dict(sorted(item_to_sort.items(),
                              key=sort_by_second_part_of_key))
    for key in sorted_item:
        if isinstance(sorted_item[key], dict) and (len(sorted_item[key]) > 1):
            sorted_item[key] = sorted_json(sorted_item[key])
    return sorted_item


def json(file_to_format, replacer='  ', spaces_count=1):
    def inner(current_value, add_indent):
        if not isinstance(current_value, dict):
            return str(check_exceptions(current_value))

        current_count = add_indent + spaces_count
        deep_indent = replacer * current_count
        current_indent = replacer * add_indent
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}"{key}": '
                         f'{inner(val, current_count)},')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return re.sub(r',(?=\n\s*})', r'', inner(sorted_json(add_sign(
        file_to_format)), 0))
