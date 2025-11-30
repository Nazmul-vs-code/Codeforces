k, r= map(int,input().split())

shovel = 0
for i in range(1,11):
    current = i*k
    if current%10==0 or current%10==r:
        shovel = i
        break
print(shovel)    