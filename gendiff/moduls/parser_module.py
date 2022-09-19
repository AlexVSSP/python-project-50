def check_for_nested_dict(nested_dict):
    dictionary = {}
    if not isinstance(nested_dict, dict):
        return nested_dict
    else:
        for key, value in nested_dict.items():
            dictionary[f'  {key}'] = check_for_nested_dict(value)
        return dictionary


def parse(first_file, second_file):
    third_file = {}
    set1 = set(first_file)
    set2 = set(second_file)

    equal_elem_in_both_files = set1 & set2
    diff_elem_in_first_file = set1 - set2
    diff_elem_in_second_file = set2 - set1

    for key in diff_elem_in_first_file:
        value = first_file[key]
        third_file[f'- {key}'] = check_for_nested_dict(value)

    for key in diff_elem_in_second_file:
        value = second_file[key]
        third_file[f'+ {key}'] = check_for_nested_dict(value)

    for key in equal_elem_in_both_files:
        if first_file[key] == second_file[key]:
            value = first_file[key]
            third_file[f'  {key}'] = value
        elif isinstance(first_file[key], dict) \
                and isinstance(second_file[key], dict):
            third_file[f'  {key}'] = parse(first_file[key], second_file[key])
        else:
            value1 = first_file[key]
            value2 = second_file[key]
            third_file[f'- {key}'] = check_for_nested_dict(value1)
            third_file[f'+ {key}'] = check_for_nested_dict(value2)
    return third_file
