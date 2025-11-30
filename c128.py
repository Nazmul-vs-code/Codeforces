t = int(input())

for _ in range(t):
    s = input().strip()
    hulf = len(s)//2
    if (s[:hulf] == s[hulf:]):
        print("YES")
    else:
        print("NO")    


