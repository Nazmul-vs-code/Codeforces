p , a = map(int,input().split())
monstar = []
condition = True

condition = True
for i in range(a):
    strength , reward = map(int,input().split())
    monstar.append((strength,reward))
monstar.sort()
for strength , reward in monstar:    
    if p > strength:
        p+=reward
    else:
        print("NO") 
        condition = False   
        break
if condition:
    print("YES")    