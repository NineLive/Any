objects = []


def foo(x):
    print('foo', x)

def bar(a,b):
    """Складывает а и б"""
    return a+b

def create_object(name: str):
    objects.append('object[' + name + ']')

def print_objects():
    for obj in objects:
        print(obj)
if __name__ == '__main__':
    print('started')
    print("Let's test it")
    if bar(2,2)==4:
        print('Ok')
    else:
        print('Fail')
