n = int(input())

def chacknum(a,b,c):
    if a + b == c or b+c == a or a+c == b :
        print("YES")
    else:
        print("NO")    
            
for i in range(n):
    t1,t2,t3 = map(int,input().split())
    chacknum(t1,t2,t3)
    