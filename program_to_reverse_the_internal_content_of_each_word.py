#write a program to reverse internal content of each word.
start = 'today is a sunny day'
second = start.split()
second1 = []
for word in second:
    second1.append(word[::-1])
print(second1)
output = ' '.join(second1)
print(output)
