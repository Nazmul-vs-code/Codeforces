t = int(input())
li = list(map(int,input().split()))

prog = []
ma = []
pe = []

for i in range(t):
    if li[i] == 1:
        prog.append(i)
    if li[i] == 2:
        ma.append(i)
    if li[i] == 3:
        pe.append(i)
teams = min(len(prog) , len(ma) , len(pe))        

print(teams)
for l in range(teams):
    print(f"{prog[l]+1} {ma[l]+1} {pe[l]+1}")