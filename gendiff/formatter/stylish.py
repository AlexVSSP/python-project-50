import itertools


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
    return element


def sorted_stylish(item_to_sort):
    sorted_item = dict(sorted(item_to_sort.items(),
                              key=sort_by_second_part_of_key))
    for key in sorted_item:
        if isinstance(sorted_item[key], dict) and (len(sorted_item[key]) > 1):
            sorted_item[key] = sorted_stylish(sorted_item[key])
    return sorted_item


def stylish(file_to_format, replacer='  ', spaces_count=1):
    def inner(current_value, add_indent):
        if not isinstance(current_value, dict):
            return str(current_value)

        current_count = add_indent + spaces_count
        deep_indent = replacer * current_count
        current_indent = replacer * add_indent
        inner_count = current_count + spaces_count
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: '
                         f'{inner(check_exceptions(val), inner_count)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return inner(sorted_stylish(file_to_format), 0)
