n = int(input())

percentages = list(map(int,input().split()))
new = 0

for i in range(n):
    new+=percentages[i]
avg = new/n
print(avg)