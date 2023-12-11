import zipfile

to_add = ['Files/hello.csv',
          'Files/Hey.csv'
          ]


def add_to_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt) as archive:
        for f in files:
            lst = archive.namelist() # gives us a list of files contained in ZIP Files
            if f not in lst:
                archive.write(f)
                print(f'File successfully added {f}')
            else:
                print(f'File already exist in ZIP: {f}')


add_to_zip('./files.zip', to_add, 'a') # a - append mode, open the existing zip file in append mode, not overriding      

