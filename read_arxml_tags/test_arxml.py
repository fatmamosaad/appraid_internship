from read_tags_from_arxml import * # type: ignore

# Example usage
arxml_file_path = get_file_path()  # Get the file path from the user
extracted_data = extract_sw_base_type_data(arxml_file_path)
output_file=r'C:\Users\ext.fatma.mosaad\Desktop\Fatma\read_xml\output.txt'
write_file(output_file, extracted_data) # type: ignore

