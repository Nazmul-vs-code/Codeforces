
t = int(input())

for _ in range(t):
    n = int(input())
    li = list(map(int,input().strip().split()))

    if len(set(li)) == n:
        print("YES")
    else:  
        print("NO")