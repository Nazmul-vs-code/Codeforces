n = int(input())
numlist = [100,20,10,5,1]
counter = 0
for i in numlist:
    count = n//i
    counter+=count
    n%=i



print(counter)    