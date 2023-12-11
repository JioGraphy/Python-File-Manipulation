import os, fnmatch
from tqdm import tqdm
import time

def match(folder, search):

    matching_files = []

    for fn in os.listdir(folder):
        if fnmatch.fnmatch(fn, search): 
            matching_files.append(fn)

    
    print(f"{len(matching_files)} file(s) found: ") # len - count and return number of items in container
    print(f"Search for: {search}")
    print("-------------------------------") 

    # Displays the file name
    for file_name in matching_files:
        print(file_name)

# print(tqdm.__le__)

# invoke the function
# match('./Location', '*.csv')
folder_path = './Location'
search_pattern = '*_test.csv'

match(folder_path, search_pattern)