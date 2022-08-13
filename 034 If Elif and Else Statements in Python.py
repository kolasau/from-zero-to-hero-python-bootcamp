try:
    number = int(input("Please enter your number: "))
    if int(number) == 1:
        print("That's 1")
    elif number == 2:
        print("That's 2")
    else:
        print("Missing 1 or 2, input 1 or 2")
    if number == int:
        pass
except ValueError:
    print("Something went wrong")