#  1st
st = 'Print only the words that start with s in this sentance'  # use split()

for word in st.split():
    if word[0] == 's':
        print(word)
print('_______________________________')
#  2nd

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
print('_______________________________')
#  3rd

sss = []
st = 'Create a list of the first letters of every word in this string'
for letter in st.split():
    if letter[0]:
        sss.append(letter[0])
print(sss)

# 3.2 same as above
asd = [word[0] for word in st.split()]
print(asd)

#  4
print(list(range(0, 11, 2)))
