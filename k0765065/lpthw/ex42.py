## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## __init__ has-a reference with Dog's name
        self.name = name

## Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## __init__ has-a reference with Cat's name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## __init__ has-a reference with Person's name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## __init__ has-a reference with Employee's name and salary
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a pet cat named Satan
mary.pet = satan

## Frank is-a employee that has-a salary of $120000
frank = Employee("Frank", 120000)

## Frank has-a pet dog named Rover
frank.pet = rover

## Flipper is-a Fish
flipper = Fish()

## Crouse is-a Salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()
