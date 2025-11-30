t = int(input())


for _ in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    summetion = sum(li)
        
    if summetion %2==0:
        print("YES")
    else:
        print("NO")    