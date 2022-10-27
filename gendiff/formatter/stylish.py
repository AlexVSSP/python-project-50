import itertools
from gendiff.parser import ADDED_ELEMENT, DELETED_ELEMENT, UNCHANGED_ELEMENT, \
    NESTED_ELEMENT, CHANGED_ELEMENT


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
    return element


def add_sign(key, val):
    if not isinstance(val, dict):
        return f'  {key}'
    if isinstance(val, dict) and len(val) == 1:
        return f'  {key}'
    elif val['type'] == DELETED_ELEMENT:
        return f'- {key}'
    elif val['type'] == ADDED_ELEMENT:
        return f'+ {key}'
    elif val['type'] == UNCHANGED_ELEMENT:
        return f'  {key}'
    elif val['type'] == CHANGED_ELEMENT and 'from' in val:
        return f'- {key}'
    elif val['type'] == CHANGED_ELEMENT and 'to' in val:
        return f'+ {key}'
    elif val['type'] == NESTED_ELEMENT:
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
        sorted_current_value = dict(sorted(current_value.items()))
        current_count = add_indent + spaces_count
        deep_indent = replacer * current_count
        current_indent = replacer * add_indent
        inner_count = current_count + spaces_count
        lines = []
        for key, val in sorted_current_value.items():
            lines.append(f'{deep_indent}{add_sign(key, val)}: '
                         f'{inner(check_except(add_value(val)), inner_count)}')
            if isinstance(val, dict) and 'to' in val:
                val.pop('from')
                lines.append(f'{deep_indent}{add_sign(key, val)}: '
                             f'{inner(check_except(add_value(val)), inner_count)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return inner(data_to_format, 0)
