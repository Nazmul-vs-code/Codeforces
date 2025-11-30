n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
num = []
new = x[1:]+y[1:]

result = True

for i in range(1,n+1):
    if i not in new:
        result = False
        break


if result:        
    print("I become the guy.")  
else:
    print("Oh, my keyboard!")