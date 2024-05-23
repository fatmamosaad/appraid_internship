from common_function_lib import *

txt_file_path = 'example.txt'
json_file_path = 'example.json'
xml_file_path = 'example.xml'
csv_file_path = 'example.csv'

txt_data = "This is a text file."
json_data = {"key": "value"}
xml_data = "<root>This is XML data.</root>"
csv_data = [['Name', 'Age'], ['Alice', 30], ['Bob', 35]]


write_file(txt_file_path, txt_data)

write_file(json_file_path, json_data)

write_file(xml_file_path, xml_data)

write_file(csv_file_path, csv_data)

print("Text File Content:")
print(read_file(txt_file_path))

# Read JSON file
print("\nJSON File Content:")
print(read_file(json_file_path))

# Read XML file
print("\nXML File Content:")
print(read_file(xml_file_path))

# Read CSV file
print("\nCSV File Content:")
print(read_file(csv_file_path))