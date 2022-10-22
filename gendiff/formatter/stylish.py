import itertools


ADDED_ELEMENT = 'added'
DELETED_ELEMENT = 'deleted'
UNCHANGED_ELEMENT = 'unchanged'
NESTED_ELEMENT = 'nested'
CHANGED_ELEMENT_FROM = 'changed from'
CHANGED_ELEMENT_TO = 'changed to'


def sorted_stylish(dict_to_sort):
    sorted_dict = dict(sorted(dict_to_sort.items()))
    for key in sorted_dict:
        if isinstance(sorted_dict[key], dict) and (len(sorted_dict[key]) > 1):
            sorted_dict[key] = sorted_stylish(sorted_dict[key])
    return sorted_dict


# flake8: noqa: C901
def check_except(element):
    if element is True:
        return "true"
    if element is False:
        return "false"
    if element is None:
        return "null"
    if isinstance(element, int):
        return element
    if '_from' in element:
        return element[:-5]
    if '_to' in element:
        return element[:-3]
    return element


def add_sign(key, val):
    if not isinstance(val, dict):
        return f'  {key}'
    if isinstance(val, dict) and len(val) == 1:
        return f'  {key}'
    elif val['type'] == 'deleted':
        return f'- {key}'
    elif val['type'] == 'added':
        return f'+ {key}'
    elif val['type'] == 'unchanged':
        return f'  {key}'
    elif val['type'] == 'changed from':
        return f'- {key}'
    elif val['type'] == 'changed to':
        return f'+ {key}'
    elif val['type'] == 'nested':
        return f'  {key}'


def add_value(val):
    if not isinstance(val, dict):
        return val
    if isinstance(val, dict) and len(val) == 1:
        return val
    elif 'value' in val:
        return val['value']
    elif 'from' in val:
        return val['from']
    elif 'to' in val:
        return val['to']


def stylish(data_to_format, replacer='  ', spaces_count=1):
    def inner(current_value, add_indent):
        if not isinstance(current_value, dict):
            return str(current_value)

        current_count = add_indent + spaces_count
        deep_indent = replacer * current_count
        current_indent = replacer * add_indent
        inner_count = current_count + spaces_count
        lines = []
        for key, val in current_value.items():
            if key == 'type':
                continue
            lines.append(f'{deep_indent}{add_sign(check_except(key), val)}: '
                         f'{inner(check_except(add_value(val)), inner_count)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return inner(sorted_stylish(data_to_format), 0)
