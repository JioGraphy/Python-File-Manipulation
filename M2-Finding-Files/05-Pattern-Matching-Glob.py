from pathlib import Path


def glob_match(folder, search):
    p = Path(folder)
    
    for n in p.glob(search):
        print(n)

'''
We are not searching for files by first listing the contents of a directory and then looking for 
specific files that match the search criteria but instead applying the search criteria to the path
of the folder to inspect
'''
    

# glob_match('./Location', '*2_*_*.*')
glob_match('./Location/sub-folder', '*1_*_*.*')
