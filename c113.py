t = int(input())

code = "codeforces"

for _ in range(t):
    counter = 0
    s = input()
    for i in range(len(s)):
        if s[i] != code[i]:
            counter += 1
    print(counter)        
    