t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    
    ok = False
    for i in range(n):
        if a[i] == k:
            ok = True
    if ok:
        print("YES")
    else:
        print("NO")    