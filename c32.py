n = int(input())

lucky_numbers= []

for i in range(1,1001):
    is_lucky = True
    for digit in str(i):
        if digit != '4' and digit != '7' :
            is_lucky = False
            break
    if is_lucky:
        lucky_numbers.append(i)

almost_lucky = False
for lucky in lucky_numbers :
    if n % lucky == 0 :
        almost_lucky = True
        break
if almost_lucky:
    print("YES") 
else:
    print("NO")       