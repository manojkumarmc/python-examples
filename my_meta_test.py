
class MyMetaClass(type):
    def __new__(mcs, name, bases, dict):
        print(mcs)
        print(name)
        print(bases)
        print(dict)
        clsobj = super().__new__(mcs, name, bases, dict)
        return clsobj


class Animal(metaclass=MyMetaClass):
    def __init__(self):
        pass

animal = Animal()

'''
<class '__main__.MyMetaClass'>
Animal
()
{'__qualname__': 'Animal', '__init__': <function Animal.__init__ at 0x7f34ddc250d0>, '__module__': '__main__'}

'''
