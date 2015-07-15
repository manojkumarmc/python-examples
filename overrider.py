#! /usr/bin/python3

from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Dog(Animal):
    def make_sound(self):
        print("Bow")



cat = Cat()
dog = Dog()

def sounder(somebody):
    somebody.make_sound()


sounder(cat)
sounder(dog)

