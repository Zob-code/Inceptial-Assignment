# animal is a object
class Animal(object):
    pass

# dog is a animal
class Dog(Animal):
    def __init__(self, name):
        # dog has a name
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        self.name = name


class Person(object):
    def __init__(self, name):
        self.name = name

        self.pet = None

class Employee(Person):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

rover = Dog("Rover")

satan = Cat("satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 25000)

frank.pet = rover


