import json

def read_print_json(fn, pretty, sort):
    with open(fn) as json_file:
        data = json.load(json_file)
        print(json.dumps(data, sort_keys=sort, indent=4)
                if pretty else data) # Ternary, shorthand of if else
        

def update_author_json(fn, arr_name, pos, key, value):
    with open(fn, 'r') as read_file:
        data = json.load(read_file)
        data[arr_name][pos][key] = value
        with open(fn, 'w') as write_file:
            json.dump(data, write_file)
    
    print(f'JSON updated successfully: ')
    print(f'"File Path: {repr(fn)} Key:{repr(key)}' )
    print(f'Change to: {repr(value)}')

# read_print_json('./files-to-read/author.json', False, False)
# read_print_json('./files-to-read/author.json', True, True)
# read_print_json('./files-to-read/author.json', True, True)


update_author_json('./files-to-read/authors-1.json', 'authors', 1, 'name', 'PySpark')

