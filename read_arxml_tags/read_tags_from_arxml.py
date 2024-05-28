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

def make_dictionary(sw_base_type):
    attributes = {filter_tag(child.tag): child.text for child in sw_base_type if child.text.strip()}
    if len(attributes) >= 5:
        short_name = attributes.get('SHORT-NAME', None)
        base_type_size = attributes.get('BASE-TYPE-SIZE', None)
        if short_name is not None and base_type_size is not None:
            return {short_name: base_type_size}
    return None
def extract_sw_base_type_data(arxml_file_path):
    try:
        tree = ET.parse(arxml_file_path)
        root = tree.getroot()
 
        # Assuming the namespace is defined as 'name_space'
        name_space = {'ns': 'http://autosar.org/schema/r4.0'}
 
        # Find all SW-BASE-TYPE elements
        sw_base_types = root.findall('.//ns:SW-BASE-TYPE', namespaces=name_space)
 
        # Extract the data you need (e.g., attribute values)
        list_of_dictionarys = []
       
        for sw_base_type in sw_base_types:
            dict_result = make_dictionary(sw_base_type)
            if dict_result is not None:
                list_of_dictionarys.append(dict_result)
               
        return list_of_dictionarys
           
    except Exception as e:
        print(f"Error parsing ARXML file: {e}")
        return None

