n = int(input())
li = []

counter1 = 0
counter2 = 0
for _ in range(n):
    team = input()
    li.append(team)
 
li.sort()    
if len(li) == 1:
    print(li[0])   
else:    
    if li.count(li[0]) > li.count(li[-1]):
        print(li[0])
    else:
        print(li[-1])    


