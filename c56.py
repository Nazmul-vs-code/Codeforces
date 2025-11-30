n = int(input())
team = []
counter = 0
for i in range(n):
    hi , ai = map(int,input().split())
    team.append((hi, ai)) #output is [(hi, ai), (hi, ai), ...]

for l in range(n):
    for k in range(n):
        if l != k:
            if team[l][0] == team[k][1]:
                counter+=1


print(counter)