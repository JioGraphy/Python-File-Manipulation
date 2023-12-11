import os, fnmatch
from tqdm import tqdm
import time

def match(folder, search):

    matching_files = []

    for fn in os.listdir(folder):
        if fnmatch.fnmatch(fn, search): 
            matching_files.append(fn)

    
    print(f"{len(matching_files)} file(s) found: ") # count the match file name
    print(f"Search for: {search}")
    print("---------------------------") 

    
    # for file_name in tqdm(matching_files):
    #     print(file_name)

    for file_name in tqdm(matching_files):
        print(file_name)
    

# invoke the function
# match('./Location', '*.csv')
# match('./Location', '*1*_file.csv')
match('./Location', '*_test.csv')