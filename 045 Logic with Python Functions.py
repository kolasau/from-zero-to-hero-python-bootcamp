def even_check(number):
    return number % 2 == 0


#  return true if any number is even inside a list
def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
    return False


def check_even_list2(num_list):
    # return all the even numbers in a list
    # placeholder variables
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers


x = check_even_list2([1, 3, 4, 5, 6, 7, 8, 9, 10])
y = check_even_list2([1, 1, 1, 1, 1])
z = check_even_list2([1, 1, 1, 3, 7, 8])
print(x)
print(y)
print(z)

