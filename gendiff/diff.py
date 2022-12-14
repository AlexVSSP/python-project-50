ADDED_ELEMENT = 'added'
DELETED_ELEMENT = 'deleted'
UNCHANGED_ELEMENT = 'unchanged'
NESTED_ELEMENT = 'nested'
CHANGED_ELEMENT = 'changed'


def find_diff(first_dict, second_dict):
    keys = {**first_dict, **second_dict}
    result = {}
    for key in keys:
        if key not in first_dict:
            result[key] = {'type': ADDED_ELEMENT, 'value': second_dict[key]}
        elif key not in second_dict:
            result[key] = {'type': DELETED_ELEMENT, 'value': first_dict[key]}
        elif first_dict[key] == second_dict[key]:
            result[key] = {'type': UNCHANGED_ELEMENT, 'value': first_dict[key]}
        elif isinstance(first_dict[key], dict) \
                and isinstance(second_dict[key], dict):
            result[key] = {'type': NESTED_ELEMENT,
                           'value': find_diff(first_dict[key],
                                              second_dict[key])}
        else:
            result[key] = {'type': CHANGED_ELEMENT, 'from': first_dict[key],
                           'to': second_dict[key]}
    return result
