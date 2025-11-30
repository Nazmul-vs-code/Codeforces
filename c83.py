n = int(input())

def odd_number(x):
    while x % 2 == 0:
        x //= 2
    if x == 1:
        print("NO")  
    else:
        print("YES") 

for _ in range(n):
    num = int(input())
    odd_number(num)     