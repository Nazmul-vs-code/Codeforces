n = int(input())
li = list(map(int,input().split()))

best = li[0]
worst = li[0]

amezing = 0
for i in range(n):
    if i != 0:
        if li[i] > best :
            amezing+=1
            best = li[i]
        elif li[i] < worst:
            amezing+=1
            worst=li[i]
print(amezing)        
