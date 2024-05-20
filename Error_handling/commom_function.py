import json
import xml.etree.ElementTree as ET
import csv

def read_file(file_path):
    try:
        # Determine the file type based on its extension
        file_extension = file_path.split('.')[-1].lower()

        if file_extension == 'txt':
            with open(file_path, 'r') as file:
                return file.read()
        elif file_extension == 'json':
            with open(file_path, 'r') as file:
                return json.load(file)
        elif file_extension == 'xml':
            tree = ET.parse(file_path)
            root = tree.getroot()
            return ET.tostring(root, encoding='utf8').decode('utf8')  
        elif file_extension == 'csv':
            with open(file_path, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                rows = []
                for row in reader:
                    rows.append(row)
                return rows
        else:
            print(f"Unsupported file type: {file_extension}")
            return None
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def write_file(file_path, data):
    try:
        # Determine the file type based on its extension
        file_extension = file_path.split('.')[-1].lower()

        if file_extension == 'txt':
            with open(file_path, 'w') as file:
                file.write(data)
        elif file_extension == 'json':
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
        elif file_extension == 'xml':
            root = ET.Element('root')
            root.text = data
            tree = ET.ElementTree(root)
            tree.write(file_path, encoding='utf-8', xml_declaration=True)
        elif file_extension == 'csv':
            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data)
        else:
            print(f"Unsupported file type: {file_extension}")
    except Exception as e:
        print(f"Error: {e}")



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