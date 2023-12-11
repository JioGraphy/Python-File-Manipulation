import shutil

def move_files(src, ds):
    shutil.move(src, ds)
    print(f'File: {src} successfully moved')

# Moving files from source to destination
# move_files('./Files/move.txt', './Files/Copy/move.txt')


# Moving folders from source to destination
# We can rename and create new folder to the destination location
move_files('./Files/Sub-folder-2', './Files/Copy')