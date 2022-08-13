mystring = 'Hello'
mylist = [letter for letter in mystring]
print(mylist)

mylist2 = [x**2 for x in range(0, 11)]
print(mylist2)

mylist3 = [num for num in range(0, 11) if num % 2 == 0]
print(mylist3)

celsius = [0, 10, 20, 34.6]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
print(fahrenheit)

fahrenheit2 = []

for temp in celsius:
    fahrenheit2.append(((9/5)*temp + 32))

print(fahrenheit2)

mylist4 = []

for num in [2, 4, 6]:
    for num2 in [100, 200, 300]:
        mylist4.append(num * num2)

print(mylist4)