n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
sum1 = 0
for i in range(m):
    sum1 += a[i]
print(abs(sum1))    