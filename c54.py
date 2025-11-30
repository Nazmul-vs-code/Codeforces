n = int(input())

earning = list(map(int, input().split()))
count = 1
max_count = 1
for i in range(1,n):

    if earning[i] >= earning[i-1]:
        count += 1
    else:
        count = 1
    max_count = max(max_count, count)    

print(max_count)            