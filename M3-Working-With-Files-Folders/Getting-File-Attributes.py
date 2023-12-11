import os
from datetime import datetime


def get_date(timestmp):
    return datetime.utcfromtimestamp(timestmp).strftime('%d %b %Y')


def get_file_attrs(folder):
    with os.scandir(folder) as dir:
        for f in dir: # loop through the folder
            if f.is_file(): # If returned is file,  returns true
                inf = f.stat() # Get the file attributes
                print(f'Modified: {get_date(inf.st_mtime)} {f.name}')


get_file_attrs('./Files/Sub-folder')

