n , m = map (int,input().split())
li = list(map(int,input().split()))

x = 1
total = 0
for i in range(m):
    y = li[i]
    if y >= x:
        time = (y - x)
        x = y
        total += time
    else:
        time = (n - (x - y))    
        x = y
        total += time


print(total)