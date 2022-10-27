from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.json import json_ as json_format


FORMAT_STYLISH = 'stylish'
FORMAT_PLAIN = 'plain'
FORMAT_JSON = 'json'


def formatter(format_, diff):
    if format_ == FORMAT_STYLISH:
        format_diff = stylish(diff)
        return format_diff
    elif format_ == FORMAT_PLAIN:
        format_diff = plain(diff)
        return format_diff
    elif format_ == FORMAT_JSON:
        format_diff = json_format(diff)
        return format_diff
