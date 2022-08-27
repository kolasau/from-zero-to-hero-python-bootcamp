# class Dog():
#
#     def __init__(self, mybreed):
#         self.my_attribute = mybreed
class Dog():

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots


my_dog = Dog(breed='Huskie', name='Sammy', spots=False)
print(my_dog)
print(my_dog.spots)
