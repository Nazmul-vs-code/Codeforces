n = int(input())
li = list(map(int,input().split()))
maximum = max(li)
counter = 0
# counter = sum(maximum - x for x in li)
for i in li:
    counter+=(maximum-i)

print(counter)