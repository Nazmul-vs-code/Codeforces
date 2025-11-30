n = int(input())


two = 2
three = 3
k = 0
li = []
if n % 2 == 0:
    k = n // 2
    for i in range(k):
        li.append(two)
else:
    current = (n - 3)//2
    li.append(three)
    for i in range(current):
        li.append(two)  
print(len(li))
print(*li)        