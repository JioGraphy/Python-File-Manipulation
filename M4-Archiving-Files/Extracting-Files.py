import zipfile
import os


def extract_file(zipf, fn, path):
    with zipfile.ZipFile(zipf, 'r') as archive: # opening a zip file in read-only mode
        archive.extract(fn, path=path)


def extract_all(zipf, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extractall(path)
        file_list = archive.namelist()
        print(f'Archive successfully extracted:')
        print(f'{file_list}')



# extract_file('./files.zip', 'Files/Hey.csv', 'extracted' )
# extract_all('./files.zip', 'extracted')