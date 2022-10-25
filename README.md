### python-project-50
[![Actions Status](https://github.com/AlexVSSP/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/AlexVSSP/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/6a419b22b1daf6cc6550/maintainability)](https://codeclimate.com/github/AlexVSSP/python-project-50/maintainability)
[![Python CI](https://github.com/AlexVSSP/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/AlexVSSP/python-project-50/actions/workflows/pyci.yml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6a419b22b1daf6cc6550/test_coverage)](https://codeclimate.com/github/AlexVSSP/python-project-50/test_coverage)

### Description of the project:

This utility accepts two JSON or YAML files as input and outputs the difference between them in formats: 'stylish', 'plain' or 'json'.

## How to install

- First you need to clone the repository:
```
    git clone git@github.com:AlexVSSP/python-project-50.git
    cd python-project-50
```
- Use commands:
```
    make install
    make build
    make package-install
```

## How to use

- To open the help menu:
```
    gendiff -h
```
- Thus, you need to enter the 'gendiff' command, specify the output format of the difference (by default, the 'stylish' format is set), and also enter the path to both files. For example:
```  
    gendiff -f plain path_to_first_file path_to_second_file
```
- Please note that utility supports file formats only with the extension .json and .yaml(.yml) 

### Comparison of flat files (JSON files)
[![asciicast](https://asciinema.org/a/518768.svg)](https://asciinema.org/a/518768)

### Comparison of flat files (yml, yaml files)
[![asciicast](https://asciinema.org/a/520143.svg)](https://asciinema.org/a/520143)

### Comparison of nested files (JSON, yaml files)
[![asciicast](https://asciinema.org/a/522370.svg)](https://asciinema.org/a/522370)

### Comparison of nested files (output in plain)
[![asciicast](https://asciinema.org/a/526834.svg)](https://asciinema.org/a/526834)

### Comparison of nested files (output in JSON)
[![asciicast](https://asciinema.org/a/531883.svg)](https://asciinema.org/a/531883)
