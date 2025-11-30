n = input()

count = 1

for i in range(1,len(n)):
    if (n[i]==n[i-1]):
        count+=1
        if count>=7:
            break   
    else:
        count = 1

if count>= 7:
    print("YES")        
else:
    print("NO")
                