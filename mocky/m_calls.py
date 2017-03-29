import requests

def m_printer(a, b):
    return '%s plus %s' % (a,b)


def add(a, b):
    return a + b

def multi(a, b):
    return a * b

def num_mgr(a, b):
    return {
        'sum': add(a, b),
        'product': multi(a, b)
    }


class Employee():

    def __init__(self, name, age, sex):
        self._name = name
        self._age = age
        self.sex = sex

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_sex(self):
        return self._sex


def get_call(url=''):
    ro = requests.get(url)
    return ro
