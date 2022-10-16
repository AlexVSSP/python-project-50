def parse(first_file, second_file):
    keys = {**first_file, **second_file}
    result = {}
    for key in keys:
        if key not in first_file:
            result[key] = {'type': 'added', 'value': second_file[key]}
        elif key not in second_file:
            result[key] = {'type': 'deleted', 'value': first_file[key]}
        elif first_file[key] == second_file[key]:
            result[key] = {'type': 'unchanged', 'value': first_file[key]}
        elif isinstance(first_file[key], dict) \
                and isinstance(second_file[key], dict):
            result[key] = {'type': 'nested', 'value': parse(first_file[key],
                                                            second_file[key])}
        else:
            result[key] = {'type': 'changed', 'from': first_file[key],
                           'to': second_file[key]}
    return result
