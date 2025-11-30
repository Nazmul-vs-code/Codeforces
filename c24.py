s = input()
t = input()
l = s[::-1]

result = True

if  len(l) == len(t):

    for i in range(len(s)) :
        if l[i] != t[i] :
            result = False
    
    if result :
        print("YES")
    else:
        print("NO")    
else:
    print("NO")
