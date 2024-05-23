import json
import csv
import xml.etree.ElementTree as ET
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
    
def write_file(file_path, data):
    try:
        # Determine the file type based on its extension
        file_extension = file_path.split('.')[-1].lower()
        if file_extension == 'txt' or file_extension == 'json':
            with open(file_path, 'w') as file:
                if file_extension == 'txt':
                    for item in data:
                        file.write(f"{item}\n")
                elif file_extension == 'json':
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