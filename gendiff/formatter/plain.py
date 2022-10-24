from gendiff.parser import ADDED_ELEMENT, DELETED_ELEMENT, UNCHANGED_ELEMENT, NESTED_ELEMENT, \
    CHANGED_ELEMENT_FROM, CHANGED_ELEMENT_TO


def sorted_plain(dict_to_sort):
    sorted_dict = dict(sorted(dict_to_sort.items()))
    for key in sorted_dict:
        if isinstance(sorted_dict[key], dict) and (len(sorted_dict[key]) > 1):
            sorted_dict[key] = sorted_plain(sorted_dict[key])
    return sorted_dict


def check_exceptions(element):
    if element is True:
        return "true"
    if element is False:
        return "false"
    if element is None:
        return "null"
    if isinstance(element, int):
        return element
    return f"'{element}'"


# flake8: noqa: C901
def display_element(data, property_, property_val, path=''):
    result = ''
    if property_val['type'] == CHANGED_ELEMENT_FROM:
        first_part = check_exceptions(property_val['from']) \
            if not isinstance(property_val['from'], dict) else '[complex value]'
        key = f'{property_[:-5]}'
        second_part_key = f'{key}_to'
        second_part = check_exceptions(data[second_part_key]['to']) \
            if not isinstance(data[second_part_key]['to'], dict) \
            else '[complex value]'
        result += f"Property '{path}{key}' was updated. " \
                  f"From {first_part} to {second_part}\n"
    if property_val['type'] == CHANGED_ELEMENT_TO:
        pass
    if property_val['type'] == UNCHANGED_ELEMENT:
        pass
    elif property_val['type'] == DELETED_ELEMENT:
        result += f"Property '{path}{property_}' was removed\n"
    elif property_val['type'] == ADDED_ELEMENT:
        value = check_exceptions(property_val['value']) \
            if not isinstance(property_val['value'], dict) \
            else '[complex value]'
        result += (f"Property '{path}{property_}' was added with value: "
                   f"{value}\n")
    elif property_val['type'] == NESTED_ELEMENT:
        path += f'{property_}.'
        for key, val in property_val['value'].items():
            result += display_element(property_val['value'], key, val, path)
    return result


def plain(data):
    sorted_data = sorted_plain(data)
    result = ''
    for key, val in sorted_data.items():
        result += display_element(sorted_data, key, val)
    result = result.strip()
    result = result.splitlines()
    result = dict.fromkeys(result)
    result = "\n".join(result)
    return result
