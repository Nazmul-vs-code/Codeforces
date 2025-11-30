t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    
    b = b[::-1]
    
    for i in range(k):
        if a[i] < b[i]:
            a[i] = b[i]
        else:    
            break
    print(sum(a))    