class Dog():
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self, how):
        print('Woof! My name is {} and I bark so {}'.format(self.name, how))


my_dog = Dog('Lab', 'Frankie')
print(my_dog.breed)
print(my_dog.name)
print(my_dog.bark('loud'))


class Circle():
    # Class object attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    # METHOD
    def get_circumference(self):
        return self.radius * Circle.pi * 2


my_circle = Circle(3)
print(my_circle.get_circumference())
print(my_circle.area)
