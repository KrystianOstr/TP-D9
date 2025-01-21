from pathlib import Path
import shutil
import os

zip_source = Path(r"C:\Users\krystian\Downloads\Project+Day+9.zip")
destination_source = Path(r"C:\Users\krystian\Downloads\p9")
file_path = destination_source / 'Instructions.txt'

def unpack_archive_shutil():
    if file_path.is_file():
        print('File exists\n')
    else:
        print('File unpacked\n')
        shutil.unpack_archive(zip_source, destination_source, 'zip')
    
def read_file():
    with open(Path(file_path), 'r') as file:
        content = file.read()
        print(content)
   
   
    
unpack_archive_shutil()
# read_file()

