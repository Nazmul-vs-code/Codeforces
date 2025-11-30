n = input()
l = input()
result= []
i = 0

while i < len(l):
    if n[i] == l[i]:
        result.append('0') 
    else:
        result.append('1') 
    i +=1    
print(''.join(result))
