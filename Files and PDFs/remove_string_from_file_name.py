import os
import re

def rename_pdf_files(folder_path):
    files = os.listdir(folder_path)
    date_pattern = re.compile(r'(\d{2})-(\d{2})-(\d{4})')

    for filename in files:
        if filename.lower().endswith('.pdf'):
            new_filename = re.sub(r'^\d{2}-\d{2}-', '', filename)
            new_filename = re.sub(date_pattern, r'\2-\1', new_filename)
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            print(f"Renamed {filename} to {new_filename}")

def remove_string_from_filenames(folder_path, string_to_remove):
    files = os.listdir(folder_path)

    for filename in files:
        if string_to_remove in filename:
            new_filename = filename.replace(string_to_remove, '')
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            print(f"Removed '{string_to_remove}' from {filename}. New filename: {new_filename}")

# Provide the folder path here
folder_path = os.getcwd()
#rename_pdf_files(folder_path)

# Provide the string to remove
string_to_remove = 'WINSEM2023-24_BSTS302P_SS_CH2023240500202_Reference_Material_I_'
remove_string_from_filenames(folder_path, string_to_remove)
