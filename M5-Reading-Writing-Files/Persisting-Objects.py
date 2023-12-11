# Serializing the class using pickle module and store in binary file
import pickle


class Person:
    age = 45
    name = 'John Smith'
    kid = ['Pete', 'Lily', 'Kate']
    employers = {'AWS': 2022, 'Microsoft': 2018, 'Yahoo': 2005}
    shoes_sizes = (11, 12)


def serialize(obj):
    pickled = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL) # Converts object into binary
    print(f'\n Serialized Object: \n{pickled}\n')
    return pickled


def deserialized(obj):
    unpickled = pickle.loads(obj)
    print(f'Deserialized: \n{unpickled}\n')
    return 


def deserialized_employers(obj):
    unpickled = pickle.loads(obj) 
    print(f'Deserialized employers: \n {unpickled.employers}\n')
    pass


# Take python object and save to binary file
def obj_to_file(fn, obj):
    with open(fn, 'wb') as pf:
        pickle.dump(obj, pf, protocol=pickle.HIGHEST_PROTOCOL)


def file_to_obj(fn, obj):
    with open(fn, 'rb') as pf:
        obj = pickle.load(pf)
        print(obj)
        return obj
    
# pickled = serialize(Person())
# deserialized(pickled)
# deserialized_employers(pickled)

obj = obj_to_file('./File-Data/person.xyz', Person())
person = file_to_obj('./File-Data/person.xyz', obj)

    