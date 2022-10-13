def sort_by_second_part_of_key(item):
    key, value = item
    sign, word = key.split(' ', maxsplit=1)
    return str(word.strip())


def define_first_part_of_key(key):
    sign, word = key.split(' ', maxsplit=1)
    return str(sign.strip())


def define_second_part_of_key(key):
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
    return f"'{element}'"


def sorted_plain(item_to_sort):
    if isinstance(item_to_sort, dict):
        sorted_item = dict(sorted(item_to_sort.items(),
                           key=sort_by_second_part_of_key))
    for key in sorted_item:
        if isinstance(sorted_item[key], dict) and (len(sorted_item[key]) > 1):
            sorted_item[key] = sorted_plain(sorted_item[key])
    return sorted_item


def display_element(file, property, property_val, path=''):
    result = ''
    sign = define_first_part_of_key(property)
    word = define_second_part_of_key(property)
    if f'- {word}' in file.keys() and f'+ {word}' in file.keys():
        first_part = check_exceptions(file[f'- {word}']) \
            if not isinstance(file[f'- {word}'], dict) else '[complex value]'
        second_part = check_exceptions(file[f'+ {word}']) \
            if not isinstance(file[f'+ {word}'], dict) else '[complex value]'
        result += f"Property '{path}{word}' was updated. " \
                  f"From {first_part} to {second_part}\n"
    elif sign == '-':
        result += (f"Property '{path}{word}' was removed\n")
    elif sign == '+':
        value = check_exceptions(property_val) \
            if not isinstance(property_val, dict) else '[complex value]'
        result += (f"Property '{path}{word}' was added with value: "
                   f"{value}\n")
    elif isinstance(property_val, dict):
        path += f'{word}.'
        for key, val in property_val.items():
            result += display_element(property_val, key, val, path)
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
