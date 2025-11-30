a1,a2,a3,a4 = map(int,input().split())

alist = [a1,a2,a3,a4]
cal = 0
s = input()
for i in range(len(s)):
    cal += alist[int(s[i])-1]
print(cal)    