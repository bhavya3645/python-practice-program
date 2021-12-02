##python program to pring the whole words in a reverse order by user
a = input('enter any string')
b = a.split()
print(b)
l1 = b[::-1]
print(l1)
output = ' '.join(l1)
print(output)

