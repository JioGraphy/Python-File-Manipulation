import zipfile

to_zip = [
        './Files/Copy/hello.csv',
        './Files/Copy/Copy.txt',
        './Files/Copy/move.txt',
        './Files/Copy/Test.txt',
        './Files/hey.csv',
]

def create_zip(zipf, files, opt): 

    # allowZip lets you archive gigabyte set as true, archive as the result of the statement
    with zipfile.ZipFile(zipf, opt, allowZip64=True) as archive: 
        for f in files:
            archive.write(f)
    
    print(f'File(s) successfully archived:')

# Parameter: name of the files, files to be archive, mode of archive
create_zip('./files.zip', to_zip, 'w')