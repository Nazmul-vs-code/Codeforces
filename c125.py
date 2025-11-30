# 12339 mod 7
# print(12339%7)

t = int(input())

for _ in range(t):
    x,y,n = map(int,input().split())
    k = n - ((n-y)%x)
    print(k)    