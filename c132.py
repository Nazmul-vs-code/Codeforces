t = int(input())

for _ in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    li.sort()
    result = 1
    small = li[0] + 1
    for i in range(1,n):
        result*=li[i]
    print(result*small)    