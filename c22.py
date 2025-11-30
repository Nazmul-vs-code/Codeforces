n = input()

n = str(n)
lucky_no =0

for digit in n:
    if digit == '4' or digit == '7':
        lucky_no+=1

luckyno = str(lucky_no)
islucky = True 

for digit in luckyno:
    if digit != '4' and digit != '7':
        islucky = False
        break

if islucky and lucky_no > 0:
    print("YES")
else:
    print("NO")        