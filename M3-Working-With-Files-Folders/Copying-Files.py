import shutil

def copy_file(fl_source, fl_destination):

    try:
        shutil.copy(fl_source, fl_destination)
        print(f'File copied successfully')
        print(f'{fl_source} ---> {fl_destination}')
    except FileNotFoundError as e:
        print(f'File not found: {e}')
    

def copy_folder(fldr_source, fldr_destination):
    
    # This function creates a new folder
    try:
        shutil.copytree(fldr_source, fldr_destination)
        print(f'Folder copied successfully')
        print(f'Folder created successfully')
        print(f'{fldr_source} Folder ---> {fldr_destination}')
    except FileExistsError as e:
        print(f'File exists: {e}')



# copy_file('./Files/Copy.txt', './Files/Sub-folder')
copy_folder('./Files', './Files/Copy-Folder-v1')