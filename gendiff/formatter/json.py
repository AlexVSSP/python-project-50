import json


ADDED_ELEMENT = 'added'
DELETED_ELEMENT = 'deleted'
UNCHANGED_ELEMENT = 'unchanged'
NESTED_ELEMENT = 'nested'
CHANGED_ELEMENT_FROM = 'changed from'
CHANGED_ELEMENT_TO = 'changed to'


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
        if val['type'] == DELETED_ELEMENT:
            new_dict[f'- {key}'] = nested_check(val['value'])
        elif val['type'] == ADDED_ELEMENT:
            new_dict[f'+ {key}'] = nested_check(val['value'])
        elif val['type'] == UNCHANGED_ELEMENT:
            new_dict[f'  {key}'] = nested_check(val['value'])
        elif val['type'] == CHANGED_ELEMENT_FROM:
            origin_key = key[:-5]
            new_dict[f'- {origin_key}'] = nested_check(val['from'])
            new_dict[f'+ {origin_key}'] = nested_check(dictionary[f'{origin_key}_to']['to'])
        elif val['type'] == CHANGED_ELEMENT_TO:
            pass
        elif val['type'] == NESTED_ELEMENT:
            new_dict[f'  {key}'] = add_sign(val['value'])
    return new_dict


def sorted_json(item_to_sort):
    sorted_item = dict(sorted(item_to_sort.items(),
                              key=sort_by_second_part_of_key))
    for key in sorted_item:
        if isinstance(sorted_item[key], dict) and (len(sorted_item[key]) > 1):
            sorted_item[key] = sorted_json(sorted_item[key])
    return sorted_item


def json_(file_to_format):
    result = sorted_json(add_sign(file_to_format))
    final_result = json.dumps(result, indent=2)
    return final_result
