#python program to reverse the string using using while loop
value = 'goodmorning'
output = ''
i = len(value)-1
while i>=0:
    output = output+value[i]
    i = i-1
print(output)
    
