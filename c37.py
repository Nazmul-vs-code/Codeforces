n = int(input())

mylist = list(map(int,input().split()))
mylist.sort(reverse=True)
count = 0
add = 0
suml = sum(mylist)
for i in range(n):
    add+=mylist[i]
    count+=1
    if add > suml/2:
        break
print(count)    