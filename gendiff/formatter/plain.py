ADDED_ELEMENT = 'added'
DELETED_ELEMENT = 'deleted'
UNCHANGED_ELEMENT = 'unchanged'
NESTED_ELEMENT = 'nested'
CHANGED_ELEMENT_FROM = 'changed from'
CHANGED_ELEMENT_TO = 'changed to'


def sorted_plain(item_to_sort):
    sorted_item = dict(sorted(item_to_sort.items()))
    for key in sorted_item:
        if isinstance(sorted_item[key], dict) and (len(sorted_item[key]) > 1):
            sorted_item[key] = sorted_plain(sorted_item[key])
    return sorted_item


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


def display_element(file, property, property_val, path=''):
    result = ''
    if property_val['type'] == 'changed from':
        first_part = check_exceptions(property_val['from']) \
            if not isinstance(property_val['from'], dict) else '[complex value]'
        key = f'{property[:-5]}'
        second_part_key = f'{key}_to'
        second_part = check_exceptions(file[second_part_key]['to']) \
            if not isinstance(file[second_part_key]['to'], dict) else '[complex value]'
        result += f"Property '{path}{key}' was updated. " \
                  f"From {first_part} to {second_part}\n"
    if property_val['type'] == 'chamged to':
        pass
    if property_val['type'] == 'unchanged':
        pass
    elif property_val['type'] == 'deleted':
        result += (f"Property '{path}{property}' was removed\n")
    elif property_val['type'] == 'added':
        value = check_exceptions(property_val['value']) \
            if not isinstance(property_val['value'], dict) else '[complex value]'
        result += (f"Property '{path}{property}' was added with value: "
                   f"{value}\n")
    elif property_val['type'] == 'nested':
        path += f'{property}.'
        for key, val in property_val['value'].items():
            result += display_element(property_val['value'], key, val, path)
    return result


def plain(file):
    sorted_file = sorted_plain(file)
    result = ''
    for key, val in sorted_file.items():
        result += display_element(sorted_file, key, val)
    result = result.strip()
    result = result.splitlines()
    result = dict.fromkeys(result)
    result = "\n".join(result)
    return result
