import pytest
from gendiff import generate_diff
from gendiff import FORMAT_PLAIN, FORMAT_JSON


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


@pytest.fixture
def file1_yml():
    return 'tests/fixtures/file1.yml'


@pytest.fixture
def file2_yml():
    return 'tests/fixtures/file2.yml'


@pytest.fixture
def file3_yaml():
    return 'tests/fixtures/file3.yaml'


@pytest.fixture
def file4_yaml():
    return 'tests/fixtures/file4.yaml'


def test_generate_diff3(file1_yml, file2_yml):
    correct_result = open('tests/fixtures/correct_result_files_1_2.txt')
    assert generate_diff(file1_yml, file2_yml) == correct_result.read()


def test_generate_diff4(file3_yaml, file4_yaml):
    correct_result = open('tests/fixtures/correct_result_files_3_4.txt')
    assert generate_diff(file3_yaml, file4_yaml) == correct_result.read()


@pytest.fixture
def file1_nested_json():
    return 'tests/fixtures/file1_nested.json'


@pytest.fixture
def file2_nested_json():
    return 'tests/fixtures/file2_nested.json'


def test_generate_nested_diff1(file1_nested_json, file2_nested_json):
    correct_result = open('tests/fixtures/correct_result_files_1_2_nested.txt')
    assert generate_diff(file1_nested_json, file2_nested_json) == correct_result.read()


def test_generate_plain_nested_diff1(file1_nested_json, file2_nested_json):
    correct_result = open('tests/fixtures/correct_plain_result_files_1_2_nested.txt')
    assert generate_diff(file1_nested_json, file2_nested_json, FORMAT_PLAIN) == correct_result.read()


def test_generate_json_nested_diff1(file1_nested_json, file2_nested_json):
    correct_result = open('tests/fixtures/correct_result_files_1_2_nested_json.txt')
    assert generate_diff(file1_nested_json, file2_nested_json, FORMAT_JSON) == correct_result.read()


@pytest.fixture
def file1_nested_yaml():
    return 'tests/fixtures/file1_nested.yaml'


@pytest.fixture
def file2_nested_yaml():
    return 'tests/fixtures/file2_nested.yaml'


def test_generate_nested_diff2(file1_nested_yaml, file2_nested_yaml):
    correct_result = open('tests/fixtures/correct_result_files_1_2_nested.txt')
    assert generate_diff(file1_nested_yaml, file2_nested_yaml) == correct_result.read()
