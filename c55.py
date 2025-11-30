n = int(input())
li = list(map(int, input().split()))

even_count = 0
odd_count = 0

for i in range(n):
    if li[i] %2 == 0:
        even_count += 1
    elif li[i] % 2 != 0:
        odd_count += 1    

for l in range(n):
    if even_count == 1:
        if li[l] % 2 == 0:
            print(l + 1)
            break
    else:
        if odd_count == 1:
            if li[l] % 2 != 0:
                print(l + 1)
                break        