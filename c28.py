n = int(input())

openieon = list(map(int,input().split()))

# openieon = []
# for i in range(n):
#     openieon.append(int(input()))  

if 1 in openieon:
    print("HARD")
else:
    print("EASY")        