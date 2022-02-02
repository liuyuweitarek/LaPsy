import jsonpickle

def util_obj2file(obj, filename):
    frozen = jsonpickle.encode(obj)
    with open(filename, 'w') as f:
        print(frozen, file = f)
        f.close()

def util_file2obj(filename):
    obj = jsonpickle.decode(open(filename, 'r').read())
    return obj
