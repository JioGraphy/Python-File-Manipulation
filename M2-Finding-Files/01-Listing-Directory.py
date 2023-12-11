# Remember the concept of relative and absolute path directory

import os

def list_dir(folder):
    for fn in os.listdir(folder): # List entries (files and folders) on the said folder path 
        print(fn) 

# list_dir('./Files')

# or 
# Passed the name of the folder that we want to list in our current project directory
# Projects current directory
list_dir('./Files')