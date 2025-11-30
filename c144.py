from math import ceil, floor


t = int(input())

for _ in range(t):
    a,b,c = map(int, input().split())
    
    anna_total = a + ceil(c/2)   
    katie_total = b + floor(c/2)
    if anna_total>katie_total:
        print("First")
        
    else:
        print("Second")    