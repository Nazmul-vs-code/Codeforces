t = int(input())

for _ in range(t):
    n = int(input())
    counter = 0
    while n != 1:
        if n %6 == 0:
            n //= 6
            
        elif n %3 == 0:
            n*= 2
        else:
            counter = -1    
            break
        counter += 1
    print(counter)    
