import os
from pathlib import Path


def rename_file_1(src, dst):
    os.rename(src, dst)
    print(f'Successfully renamed the file: {src} ---> {dst}')

def rename_file_2(src, dst):
    f = Path(src)
    f.rename(dst)
    print(f'Successfully renamed the file: {src} ---> {dst}')


# rename_file_1('./Files/Test.txt', './Files/Text.txt')
rename_file_2('./Files/Text.txt', './Files/Test.txt')