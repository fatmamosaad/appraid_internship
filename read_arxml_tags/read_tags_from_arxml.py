import json
import csv
import os
import re
from xml.etree import ElementTree as ET
import tkinter as tk
from tkinter import filedialog

#This function used to filter non required tag from the tag name
def filter_tag(input_string):
    pattern = r"\}(.*?)$"
    match = re.search(pattern, input_string)
    if match:
        captured_value = match.group(1)
        return captured_value
    
def get_file_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    print(f"File selected: {file_path}")
    return file_path

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
        elif file_extension == 'xml' or file_extension == 'arxml':  # Allowing both 'xml' and 'arxml'
            tree = ET.parse(file_path)
            root = tree.getroot()
            return root
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
    
def extract_sw_base_type_data(arxml_file_path):
    try:
        tree = ET.parse(arxml_file_path)
        root = tree.getroot()

        # Assuming the namespace is defined as 'ns'
        ns = {'ns': 'http://autosar.org/schema/r4.0'}

        # Find all SW-BASE-TYPE elements
        sw_base_types = root.findall('.//ns:SW-BASE-TYPE', namespaces=ns)

        # Extract the data you need (e.g., attribute values)
        data_list = []
        for sw_base_type in sw_base_types:
            attributes = {}
            for child in sw_base_type:
                attributes[child.tag] = child.text
                if(child.text == "\n                    "):
                    pass
                else:
                    data_list.append([filter_tag(child.tag),child.text])

        return data_list
    except Exception as e:
        print(f"Error parsing ARXML file: {e}")
        return None

    
def write_file(file_path, data):
    try:
        # Determine the file type based on its extension
        file_extension = file_path.split('.')[-1].lower()

        if file_extension == 'txt':
            with open(file_path, 'w') as file:
                for item in data:
                    file.write(f"{item}\n")
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

# Example usage
arxml_file_path = get_file_path()  # Get the file path from the user
extracted_data = extract_sw_base_type_data(arxml_file_path)
print(f"data:{extracted_data}")
if extracted_data:
   write_file(r'C:\Users\ext.fatma.mosaad\Desktop\Fatma\read_xml\output.txt', extracted_data)

