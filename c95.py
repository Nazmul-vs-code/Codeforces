t = int(input())

for i in range(t):
    a,b,c = map(int,input().split())
    li = [a,b,c]
    for l in range(3):
        if li.count(li[l]) == 1:
            print(li[l])