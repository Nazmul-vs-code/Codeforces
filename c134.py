t=int(input())

for _ in range(t):
    n, x = map(int,input().split())
    li = list(map(int,input().split()))
    n_li = []
    
    n_li.append(li[0])
    for i in range(1,n):
        min = li[i]-li[i-1]
        n_li.append(min)
    n_li.append(2*(x-li[-1]))    
    print(max(n_li))