t = int(input())

for _ in range(t):
    n = int(input())
    if n%4 != 0:
        print("NO")
    else:
        print("YES")
        a = []
        b = []
        for i in range(1,(n//2)+1):
            a.append(2*i)   
        sum1 = sum(a)  
        for i in range(1,(n//2)+1):
            b.append(2*i - 1)               
        sum2 = sum(b)
        if sum1 != sum2:
            b[-1] += (sum1 - sum2)
        result = a + b
        print(*result)    
