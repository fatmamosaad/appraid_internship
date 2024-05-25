# File Operations Script

This script is designed to read and write files in different formats. It supports text, JSON, XML, and CSV files.

## Features

- **Read File**: This function takes a file path as input and reads the file based on its extension. It supports 'txt', 'json', 'xml', 'arxml', and 'csv' files. If the file type is unsupported or an error occurs during reading, it prints an error message.

- **Write File**: This function takes a file path and data as input and writes the data to the file based on its extension. It supports 'txt', 'json', 'xml', and 'csv' files. If the file type is unsupported or an error occurs during writing, it prints an error message.

## Usage

You can use this script to read and write files in your Python projects. Just import the `read_file` and `write_file` functions from this script and use them in your code.

For example, to write data to a JSON file and then read it, you can do:

```python
from common_function_lib import *

json_file_path = 'example.json'
json_data = {"key": "value"}

write_file(json_file_path, json_data)
print(read_file(json_file_path))