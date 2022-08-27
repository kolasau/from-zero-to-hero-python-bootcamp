class Animal():

    def __init__(self):
        print('Animal created')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')


#  derived class
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def eat(self):
        print('I am a dog and eating')

    #  overwriting the old method
    # def who_am_i(self):
    #     print('I am a dog!')
    def bark(self):
        print('WOOF!')


mydog = Dog()
print(mydog.bark())
print(mydog.eat())
# myanimal = Animal()
# myanimal.eat()
# myanimal.who_am_i()
# mydog = Dog()
# mydog.eat()
# mydog.who_am_i()
# myanimal.who_am_i()

#
