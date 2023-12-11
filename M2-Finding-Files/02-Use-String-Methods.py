import os

def ends_with(folder, search):
    for fn in os.listdir(folder):
        if fn.endswith(search):
            print(fn)

def stars_with(folder, search):
    for fn in os.listdir(folder):
        if fn.startswith(search):
            print(fn)


# ends_with('./Location', '.csv')

stars_with('./Location', 'Test')

# try:

#     ends_with('./Location', '.txt')
#     print('File Found')
    
# except FileNotFoundError as e:

#     print(e, 'File not found or does not exist')
    