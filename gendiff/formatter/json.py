import json


def json_(data_to_format):
    final_result = json.dumps(data_to_format, indent=2)
    return final_result
