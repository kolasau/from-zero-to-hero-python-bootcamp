with open('test.txt', mode='w') as f:
    f.write('Hello World')

with open('test.txt', mode='r') as r:
    print(r.read())

x = open('my_exe_file.txt', mode='w')
x.write('Hello My Friends!')
x.close()

with open('my_exe_file.txt', mode='r') as trying_to_read:
    print(trying_to_read.read())


