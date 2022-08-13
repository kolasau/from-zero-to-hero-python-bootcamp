# myfile = open('mytxtfile.txt')
# print(myfile.read())
# print(myfile.read())  # here is the empty result bcoz cursor is in the end of the file after first reading
#
# myfile.seek(0)  # resets the cursor to the beginning
# print('------------------')
# contents = myfile.read()  # here I can save all the data from myfile.txt in 'contents' variable
# print(contents)
#
# mypic = open('/home/maksim/Downloads/London.ovpn')
# print(mypic.read())
# myfile.close()
# mypic.close()
# print('DONE')
#
with open('mytxtfile.txt') as my_file_txt:
    contents = my_file_txt.read()
    print(contents)

with open('mytxtfile.txt', mode='r') as myfile:
    contents2 = myfile.read()
    print(contents2)

with open('my_new_file.txt', mode='r') as f:
    print(f.read())
print('________________________________')
with open('my_new_file.txt', mode='a') as fa:
    fa.write('\nFOUR ON FOURTH')

with open('my_new_file.txt', mode='r') as r:
    print(r.read())
with open('creating a new file.txt', mode='w') as w:
    print(w.write('my name is MAKSIM'))

with open('creating a new file.txt', mode='r') as reading:
    print(reading.read())