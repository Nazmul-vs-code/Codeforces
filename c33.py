n = int(input())
mlist = []

gruoup_count = 1

for i in range(n):
    megnet = input()
    mlist.append(megnet)

for l in range(1,n):
    if mlist[l]  != mlist[l-1]:
        gruoup_count+=1  
print(gruoup_count)        