n = int(input())
dali = []
new = str(n)
counter = 0
for i in range(len(new)):
    if new[i] != '0':
        dali.append(int(new[i])*10**(len(new)-i-1))
        counter+=1


print(counter)
print(*dali)            