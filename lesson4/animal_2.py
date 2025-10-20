"""
Допишите код под условия в цикле так, чтобы вывод был корректным
"""

class Animal:

    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name} is walking')


class Dog(Animal):

    def bark(self):
        print('Bark!')


class Cat(Animal):

    def meow(self):
        print('Meow!')



animals = [Dog('Dog1'), Dog('Dog2'), Cat('Cat1'), Dog('Dog3')]

for animal in animals:
    if isinstance(animal, Dog):
        animal.bark()
    elif isinstance(animal, Cat):
        animal.meow()
