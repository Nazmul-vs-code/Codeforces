n = int(input())
s = input()
s = s.upper()

A = 0
D = 0

for i in s:
    if i != 'A' :
        D+=1
    else:
        A+=1    

if A>D:
    print("Anton")
elif D>A:
    print("Danik")

elif D == A:
    print("Friendship")        
