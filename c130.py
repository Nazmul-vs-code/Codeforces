n = int(input())

level = 0
counter = 0

for i in range(1,n+1):
    needed = i * (i+1)//2
    counter += needed
    if counter > n:
        break
    level += 1

print(level)
