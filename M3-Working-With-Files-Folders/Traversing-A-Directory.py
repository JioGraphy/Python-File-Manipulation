import os

# Walk can be used in a nested subfolders and files
# Traversing a directory is done by looping through all the folder paths, directories and files.
def traverse(folder):

    '''
    Walk method performs traversing to the specified folder and returns all the sub folder parts, 
    directories, files contained in the specified folder, all in one shot
    '''
    for fldpath, dirs, fls in os.walk(folder):
        print(f'Folder: {fldpath}')
        for fn in fls:
            print(f'\t{fn}')

traverse('./Files')

