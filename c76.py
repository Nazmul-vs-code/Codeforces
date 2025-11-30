a , b = map(int,input().split())

li = [a , b]
li.sort()
if li[0] != li[1]:
    fationable_day = li[0]
    new = li[1] - li[0]
    new1 = new//2
    print(fationable_day,new1)
else:
    print(li[0],0)