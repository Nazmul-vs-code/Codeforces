t = int(input())

for _ in range(t):
    h,m = map(int,input().split())
    remaining_h = 24 - h
    remaining_m = (remaining_h*60) - m
    print(remaining_m)