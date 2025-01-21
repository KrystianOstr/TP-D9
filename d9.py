from pathlib import Path
import shutil
import os
import re
import time
import math
import datetime

zip_source = Path(r"C:\Users\krystian\Downloads\Project+Day+9.zip")
destination_source = Path(r"C:\Users\krystian\Downloads\p9")
file_path = destination_source / 'Instructions.txt'
pattern = r'N[a-zA-Z]{3}-\d{5}'
numbers_found = 0


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
   
def os_walk_read_file(file_to_search, pattern):
    global numbers_found
    with open(Path(file_to_search), 'r') as file:
        content = file.read()
        match = re.search(pattern, content)
        
        if match:
            numbers_found += 1
            print(f'{file_to_search.name} \t {match.group()}')
        
        
        
    
unpack_archive_shutil()
# read_file()
# os_walk_read_file(file_path, pattern)

current_date = datetime.datetime.now().strftime("%d-%m-%y")

print(f'Search date: {current_date}\n')

print('FILE\t\tSERIAL NO.')
print('----\t\t----')


search_start = time.time()

for folder, subfolder, files in os.walk(destination_source):
    for file in files:
        if file == 'Instructions.txt': #Pomijam bo taki jest zamysl.
            continue
        
        file_path = Path(folder) / file
        os_walk_read_file(file_path, pattern)

search_end = time.time()

running_time = search_end - search_start
duration = math.ceil(running_time)

print(f'Numbers found: {numbers_found}')
print(f'It took {duration} second/s')