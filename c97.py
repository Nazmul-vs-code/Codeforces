t = int(input())

for i in range(t):
    n = int(input())
    number = 1
    count = 0 
    while True:
        if number%3 != 0 and number%10 !=3:
            count+=1
            if count == n :
                print(number) 
                
                break
        number+=1    