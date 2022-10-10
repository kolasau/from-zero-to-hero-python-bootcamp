try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print('Type Error')
finally:
    print("You can't square a letters")

print("-----------------------------------------------------------------")


try:
    x = 5
    y = 0
    z = x / y
except ZeroDivisionError:
    print("You can't divide by zero")
finally:
    print('All done')
print("-----------------------------------------------------------------")


def ask():
    while True:
        try:
            result = int(input("Input an integer: "))
            square = result ** 2
        except ValueError:
            print("Something went wrong, please input an integer")
            continue
        else:
            print(f'Thank you, your number is {square}')
            break



ask()