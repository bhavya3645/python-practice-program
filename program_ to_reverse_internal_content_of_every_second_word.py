#program to reverse internal content ofevery second word present in the given string. 
first = 'i live in ratlam'
l = first.split()
i = 0 
l1 = []
while i<len(l):
    if i%2 == 0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i = i+1 
print(l1)
