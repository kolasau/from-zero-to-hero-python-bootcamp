def myfunc(input_string):
    newstring = ''
    for item, letter in enumerate(input_string):
        if item % 2 == 0 or item == 0:
            newstring = newstring + letter.lower()
        else:
            newstring = newstring + letter.upper()

    return newstring


x = myfunc('Anthropomorphism')
print(x)