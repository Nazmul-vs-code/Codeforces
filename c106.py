t = int(input())

li = "abc"
count = 0

for _ in range(t):
    abc = input()
    for i in range(3):
        if abc[i] != li[i]:
            count+=1
    if count <=2:
        print("YES")        
    else:
        print("NO")    
    count = 0    