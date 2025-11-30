t = int(input())
for _ in range(t):
    a , b , c , d = map(int, input().split())
    counter = 0
    
    if a < b :
        counter += 1
    if a < c:
        counter += 1 
    if a < d:
        counter += 1
   
    print(counter)