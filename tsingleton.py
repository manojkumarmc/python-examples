
def SingleTon(cls):
    instances = {}
    def checker():
        if instances.get(cls, None) == None:
            instances[cls] = cls()
        return instances[cls]
    return checker

class Emp():
    def __init__(self):
        self.name = ''
        self.age = ''

if __name__ == '__main__':
    import pdb;pdb.set_trace()
    e1 = SingleTon(Emp)()
    e1.name = 'Manoj'
    e1.age = 40

    e2 = SingleTon(Emp)()
    print e2.name

