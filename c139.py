t = int(input())
for _ in range(t):
    ok = True

    n = int(input())
    s = input()
    
    set_of = set()
    current = s[0]
    
    for i in s:
        if i != current:
            set_of.add(current)
            if i in set_of:
                ok = False
                break
            current = i 
    print("YES" if ok else "NO")    