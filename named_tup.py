from collections import namedtuple

Person = namedtuple('Person', 'name, age, sex')

p1 = Person(name='Manoj', age=18, sex='M')

print p1.name
print p1.age
print p1.sex

