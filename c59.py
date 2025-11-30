n , m = map(int,input().split())

stringl = ["."]*m
for i in range(1,n+1):
    if i%2 != 0:
        print(m*"#")
    else:
        if i%4 == 2:
            stringl[-1] = "#"
        elif i%4 == 0:
            stringl[0] = "#"   
        string ="".join(stringl)     
        print(string)    
        stringl = ["."]*m