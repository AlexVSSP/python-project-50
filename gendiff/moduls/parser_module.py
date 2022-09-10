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


def parse(first_file, second_file):
    third_file = {}
    diff_result = ''
    indent = '  '

    set1 = set(first_file.items())
    set2 = set(second_file.items())
    equal_elem_in_both_files = dict(set1 & set2)
    diff_elem_in_first_file = dict(set1 - set2)
    diff_elem_in_second_file = dict(set2 - set1)
    for key, value in equal_elem_in_both_files.items():
        third_file[f'  {key}'] = value
    for key, value in diff_elem_in_first_file.items():
        third_file[f'- {key}'] = value
    for key, value in diff_elem_in_second_file.items():
        third_file[f'+ {key}'] = value
    sorted_third_file = dict(sorted(third_file.items(),
                             key=sort_by_second_part_of_key))
    for key, value in sorted_third_file.items():
        diff_result += f'{indent}{key}: {check_exceptions(value)}\n'
    return f'{{\n{diff_result}}}'
