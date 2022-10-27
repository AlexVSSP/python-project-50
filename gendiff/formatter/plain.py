from gendiff.diff import ADDED_ELEMENT, DELETED_ELEMENT, UNCHANGED_ELEMENT, \
    NESTED_ELEMENT, CHANGED_ELEMENT


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
def display_element(data):
    def inner(property_, property_val, path=''):
        result = ''
        if property_val['type'] == CHANGED_ELEMENT:
            first_part = check_exceptions(property_val['from']) \
                if not isinstance(property_val['from'], dict) \
                else '[complex value]'
            second_part = check_exceptions(property_val['to']) \
                if not isinstance(property_val['to'], dict) \
                else '[complex value]'
            result += f"Property '{path}{property_}' was updated. " \
                      f"From {first_part} to {second_part}\n"
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
            sorted_property_val = dict(sorted(property_val['value'].items()))
            for key_, val_ in sorted_property_val.items():
                result += inner(key_, val_, path)
        return result
    final_result = ''
    sorted_dict = dict(sorted(data.items()))
    for key, val in sorted_dict.items():
        final_result += inner(key, val)
    return final_result


def plain(data):
    result = display_element(data)
    result = result.strip()
    result = result.splitlines()
    result = dict.fromkeys(result)
    result = "\n".join(result)
    return result
