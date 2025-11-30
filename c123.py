t = int(input())

for _ in range(t):
    counter = 0
    k = []
    n = int(input())
    li = input()
    for i in li:
        if i not in k:
            k.append(i)
            counter+=2
        else:
            k.append(i)
            counter+=1    
    print(counter)            