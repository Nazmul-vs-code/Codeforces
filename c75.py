x1 , x2 , x3 , x4 = map(int,input().split())

li = [x4,x2,x3,x1]

a = max(li) - x1
b = max(li) - x2
c = max(li) - x3
d = max(li) - x4
new = [a , b , c ,d]
new.sort()
del new[0]
print(*new)
