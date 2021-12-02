#python program to pring the whole words in a reverse order
a = 'today is very sunny day'
b = a.split()
print(b)
l1 = b[::-1]
print(l1)
output = ' '.join(l1)
print(output)

