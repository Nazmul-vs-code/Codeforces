x1,x2,x3 = map(int,input().split())

li = [x1,x2,x3]
li.sort()

m = li[1]
result = abs(x1-m) + abs(x2-m) + abs(x3-m)
print(result)