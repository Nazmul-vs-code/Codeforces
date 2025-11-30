x = int(input())
el_step = [1,2,3,4,5]

full_step = x//5
leftover = x%5
if leftover == 0:
    print(full_step)

else:
    print(full_step+1)    