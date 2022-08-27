class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'


class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says meow!'


niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())

for pet_class in [niko, felix]:
    print(pet_class)
    print(pet_class.speak())


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)

print('---------------------------------------------------------------------------------------------------------------')


class Animal():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')


class Dog(Animal):

    def speak(self):
        return self.name + ' says woof!'


class Cat(Animal):

    def speak(self):
        return self.name + ' says meow!'


fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())