
def read_text(fn):
    with open(fn) as f:
        print(f.read())


def read_text_by_line(fn):
    with open(fn) as f:
        lines = f.readlines()
        for line in lines:
            print(line, end='')
            line = f.readline()


def write_new_txt(fn, str):
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(str)
    print(f'Write successfully --> {fn}')
    
 

def append_line_txt(fn, str):
    with open(fn, 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write(str)


# read_text('./files-to-read/nested-loops.py')
# read_text_by_line('./files-to-read/nested-loops.py')
# write_new_txt('./files-to-read/example.txt', 'This is sample text 1')
append_line_txt('./files-to-read/example.txt', 'This is sample text 2')



