import json


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


def generate_diff(json_file1, json_file2):
    with open(json_file1) as json.file1:
        file1 = json.load(json.file1)
    with open(json_file2) as json.file2:
        file2 = json.load(json.file2)
    file3 = {}
    diff_result = ''
    indent = '  '

    set1 = set(file1.items())
    set2 = set(file2.items())
    equal_elem_in_both_files = dict(set1 & set2)
    diff_elem_in_file1 = dict(set1 - set2)
    diff_elem_in_file2 = dict(set2 - set1)
    for key, value in equal_elem_in_both_files.items():
        file3[f'  {key}'] = value
    for key, value in diff_elem_in_file1.items():
        file3[f'- {key}'] = value
    for key, value in diff_elem_in_file2.items():
        file3[f'+ {key}'] = value
    sorted_file3 = dict(sorted(file3.items(), key=sort_by_second_part_of_key))
    for key, value in sorted_file3.items():
        diff_result += f'{indent}{key}: {check_exceptions(value)}\n'
    return f'{{\n{diff_result}}}'
