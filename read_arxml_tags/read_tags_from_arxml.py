import json
import csv
import re
from xml.etree import ElementTree as ET
import tkinter as tk
from tkinter import filedialog
from common_function_lib import * # type: ignore

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

    
# Example usage
arxml_file_path = get_file_path()  # Get the file path from the user


extracted_data = extract_sw_base_type_data(arxml_file_path)

listOfDicts = [] 

for i in range(0,len(extracted_data)-5,5):
    
    listOfDicts.append(dict(shortName = extracted_data[i][1],category = extracted_data[i+1][1],baseTypeSize = extracted_data[i+2][1],baseTypeEncoding = extracted_data[i+3][1],nativeDeclaration = extracted_data[i+4][1]))  
output_file=r'C:\Users\ext.fatma.mosaad\Desktop\Fatma\read_xml\output.txt'
write_file(output_file, listOfDicts) # type: ignore

