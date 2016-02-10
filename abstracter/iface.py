
from abc import ABCMeta, abstractmethod

class IAnimal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name):
        pass

    @abstractmethod
    def make_sound(self):
        pass

#cat = IAnimal('Pepper')
#Traceback (most recent call last):
#  File "iface.py", line 14, in <module>
#    cat = IAnimal('Pepper')
#TypeError: Can't instantiate abstract class IAnimal with abstract methods __init__, make_sound
#(img-p27)mmyalipu@localhost:[abstracter] (master) $ vim iface.py

class Cat(IAnimal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Meow")

pcat = Cat('Pepper')
pcat.make_sound()


