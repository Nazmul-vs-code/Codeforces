t = int(input())

for _ in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    eaten = 0
    small_elem = min(li)
    for i in li:
        eaten += (i-small_elem)
    print(eaten)    