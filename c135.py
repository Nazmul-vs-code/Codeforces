t = int(input())

for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    result = max(li) - min(li)
    print(result)