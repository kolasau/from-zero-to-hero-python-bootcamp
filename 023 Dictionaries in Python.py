my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict['key1'])

price_lookup = {'apples': 2.99, 'oranges': 1.9, 'milk': 5.80}
print(price_lookup['apples'])

d = {'k1': 123, 'k2': ['app', 'app2'], 'k3': {'k1.1': 123123123}}
print(d['k2'])
print(d['k3']['k1.1'])
print(d['k2'][0])

b = {'key1': ['a', 'b', 'c']}
print(b['key1'][2].upper())

c = {'k1': 100, 'k2': 200, 'k3': 300}
c['k3'] = 400
c['k1'] = 'NEW'
print(c)

a = {'k1': 100, 'k2': 200, 'k3': 300}
print(a.keys())
print(a.values())
print(a.items())



# {'Monday': 16, 'Tuesday': 17, 'Wednesday': 18}

