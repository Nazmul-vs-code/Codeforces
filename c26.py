n = int(input())
remain = 0
max_capacity = 0
for i in range(n):
    ai , bi = map(int,input().split())
    remain = (remain - ai)+bi
    
    if max_capacity<remain:
        max_capacity = remain
print(max_capacity)        