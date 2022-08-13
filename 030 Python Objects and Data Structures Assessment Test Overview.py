import math

x = 3 + 1.5 + 4
print(type(x))
d = 49
f = 5 ** 2
print(f)
print(math.sqrt(d))
s = 'Hello'
print(s[1])
print(s[::-1])
print(s[4])
print(s[-1])
list3 = [1, 2, [3, 4, 'hello']]
list3[2][2] = 'goodbye'
print(list3)
list4 = [5, 3, 4, 6, 1]
list4.sort()
print(list4)
d3 = {'simple_key': 'hello'}
print(d3['simple_key'])
d4 = {'k1': {'k2': 'hello'}}
print(d4['k1']['k2'])
mylist = [0, 0, 0]
print(mylist)

dict1 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(dict1['k1'][0]['nest_key'][1][0])
dict2 = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
print(dict2['k1'][2]['k2'][1]['tough'][2])

dict3 = {'k1': 3, 'k3': '123', 'k2': 0.123123123123}
print(sorted(dict3))

list5 = [1, 2, 33, 4, 4, 11, 22, 3, 3, 2]
print((set(list5)))

l_one = [1, 2, [10, 4]]
l_two = [1, 2, {'k1': 4}]

f = l_one[2][0] >= l_two[2]['k1']
print(f)