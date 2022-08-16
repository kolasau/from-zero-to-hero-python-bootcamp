import numpy
import string
from math import pi


def vol(rad):
    return (4.0 / 3.0) * pi * (rad ** 3)


x = vol(2)
print(x)


def ran_check(num, low, high):
    if low < num < high:
        print(f'{num} is in the range between {low} and {high}')
    else:
        print('{} is not in the range between {} and {}'.format(num, low, high))


ran_check(5, 2, 7)


def up_low(string):
    num_of_up = []
    num_of_low = []
    for i in string:
        if i.isupper():
            num_of_up.append(i)
        elif i.islower():
            num_of_low.append(i)
        else:
            pass
    return 'Number of Upper case characters: ' + str(len(num_of_up)) + '\n' + 'Number of Lower ' \
                                                                              'case characters: ' + str(len(num_of_low))


u = up_low('Hello, Mr. Rogers, how are you this fine Tuesday?')
print(u)


def unique_list(my_list):
    unique = set(my_list)
    unique_l = []
    for el in unique:
        unique_l.append(el)
    return unique_l


sample_list = [1, 1, 1, 1, 7, 10, 2, 2, 3, 3, 3, 3, 4, 5]
y = unique_list(sample_list)
print(y)


def multiply(list_of_numbers):
    result = numpy.prod(list_of_numbers)
    return result


sample_l1 = [1, 2, 3, -4, 10]
o = multiply(sample_l1)
print(o)


def palindrome(word):
    spl = word.replace(' ', '')
    return spl == spl[::-1]


t = palindrome('nurses run')
print(t)
print('--------------------------------------------------------------------------------------')


def ispangram(str1, alphabet=string.ascii_lowercase):
    #  Create a set of the alphabet
    alphaset = set(alphabet)
    #  Remove any spaces from the input string
    str1 = str1.replace(' ', '')
    #  Convert into all lowercase
    str1 = str1.lower()
    #  Grab all unique letters from the string set()
    str1 = set(str1)
    #  Alphabet set == String set input
    return str1 == alphaset


pangram = 'The quick brown fox jumps over the lazy dog'
pngr = ispangram(pangram)
print(pngr)
