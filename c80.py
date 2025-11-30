t = int(input())

for i in range(t):
    num = input()
    if int(num[0])+int(num[1])+int(num[2]) == int(num[3])+int(num[4])+int(num[5]):
        print("YES")
    else:
        print("NO")    