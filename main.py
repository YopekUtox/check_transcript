from re import sub
from pathlib import Path
from typing import Set
samples_path:  Path = Path('wavs')
list_path:  Path = Path('list.txt')

samples: Set[str] = {str(i).replace('\\','/') for i in samples_path.iterdir() if i.is_file()}
with open(list_path, 'r', encoding='utf8') as f: 
    files_in_list: Set[str] = {sub(r"\|.+","", i).strip() for i in f.readlines()}


common_part: Set[str]= samples.intersection(files_in_list)
missing_files: Set[str] = files_in_list.difference(common_part)
redundant_files: Set[str] = samples.difference(common_part)

if missing_files: 
    print("Files in transcript, which doesn't exists: ",*missing_files , sep='\n', end='\n'*2)
if redundant_files: 
    print("Files not in list: ", *redundant_files, sep='\n', end='\n'*2)

if not redundant_files and not missing_files: 
    print("All good")
