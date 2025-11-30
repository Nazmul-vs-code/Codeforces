n = int(input())
li = list(map(int,input().split()))
Sereja = 0
Dima = 0
r = n-1
l = 0
tern = True 
for _ in range(n):
    if li[l] < li[r]:
        pick = li[r]
        r-=1
    else:
        pick=li[l]
        l+=1

    if tern:
        Sereja+=pick
        
    else:
        Dima+=pick
        
    tern = not tern
    
        
print(Sereja,Dima)        