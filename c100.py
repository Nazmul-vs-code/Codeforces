n,k = map(int,input().split())
li = list(map(int,input().split()))

help = []

for i in range(n):
    recent = li[i]+k
    if recent <= 5:
        help.append(li[i])
          
print(len(help)//3)
