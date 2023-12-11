# importing module
import os


def remove_files(f):
    if os.path.isfile(f):
        try:
            os.remove(f)
            print(f'File: "{f}" successfully deleted')
        except OSError as e:
            print(f'Error: {f} : {e.strerror}')
    else:
        print(f'Error: "{f}" is not a valid file or does not longer exist')


remove_files('./Files/Copy.txt')