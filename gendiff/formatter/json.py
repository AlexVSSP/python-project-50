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
    return re.sub(r',(?=\n\s*})', r'', inner(sorted_json(file_to_format), 0))
