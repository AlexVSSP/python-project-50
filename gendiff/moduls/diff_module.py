import json

def sort_by_second_part_of_key(item):
    key, value = item
    sign, word = key.split(' ', maxsplit=1)
    return str(word.strip())


def generate_diff(json_file1, json_file2):
    with open(json_file1) as json.file1:
        file1 = json.load(json.file1)
    with open(json_file2) as json.file2:
        file2 = json.load(json.file2)

    file3 = {}
    result = ''
    indent = '  '

    for key1, value1 in file1.items():
        if key1 in file2:
            if file1[key1] == file2[key1]:
                file3[f'  {key1}'] = file1[key1]
            else:
                file3[f'- {key1}'] = file1[key1]
                file3[f'+ {key1}'] = file2[key1]
        else:
            file3[f'- {key1}'] = file1[key1]
    for key2, value2 in file2.items():
        if key2 not in file1:
            file3[f'+ {key2}'] = file2[key2]
        else:
            continue
    sorted_file3 = dict(sorted(file3.items(), key=sort_by_second_part_of_key))
    for key, value in sorted_file3.items():
        result += f'{indent}{key}: {value}\n'
    result = result.replace('F', 'f')
    result = result.replace('T', 't')
    return f'{{\n{result}}}'
