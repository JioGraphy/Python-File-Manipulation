import os, fnmatch
from datetime import datetime

from tqdm import tqdm


def match(folder, search):

    current_dt = datetime.now()
    matching_files = []

    for fn in os.listdir(folder):
        if fnmatch.fnmatch(fn, search): 
            matching_files.append(fn)

    
    print(f"{len(matching_files)} file(s) found: ") # count the match file name
    print(f"Search String Criteria: {repr(search)}")
    print(current_dt) 
    print("---------------------------")
    


    for file_name in matching_files:
        print(file_name)
    

# invoke the function
# match('./Location', '*.csv')
# match('./Location', '*1*_file.csv')
# match('./Location', '*_test.csv')

# Search for file name that contain '_test' that starts with any substring and are of any file type extension
# Asterisk - Wildcard
# match('./Location', '*_test*.*')

# only file names that include _test_ will be returned
# match('./Location', '*_test_*.*')

# combination of fnmatch, wildcards and various substrings is possible to narrow down to search the file
match('./Location', '*2_*_*.*')