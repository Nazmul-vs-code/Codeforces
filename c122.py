t = int(input())

for _ in range(t):
    n , k = map(int,input().split())
    a = list(map(int,input().split()))
    sort = sorted(a)
    
    if k > 1 or a == sort:
        print("YES")
    else:
        print("NO")    