import pytest
from gendiff import generate_diff


@pytest.fixture
def file1_json():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def file2_json():
    return 'tests/fixtures/file2.json'


@pytest.fixture
def file3_json():
    return 'tests/fixtures/file3.json'


@pytest.fixture
def file4_json():
    return 'tests/fixtures/file4.json'


def test_generate_diff(file1_json, file2_json):
    correct_result = open('tests/fixtures/correct_result_files_1_2.txt')
    assert generate_diff(file1_json, file2_json) == correct_result.read()

def test_generate_diff2(file3_json, file4_json):
    correct_result = open('tests/fixtures/correct_result_files_3_4.txt')
    assert generate_diff(file3_json, file4_json) == correct_result.read()
