guest = input()
host = input()
combination = input()

new = guest + host


if sorted(new) == sorted(combination):
    print("YES")
else:
    print("NO")    