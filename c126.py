t = int(input())

for _ in range(t):
    ok = True
    timur = sorted("Timur")
    n = int(input())
    s = input().strip()
    s = sorted(s)
    if n != 5:
        ok = False
    else:
        if s == timur:
            ok = True  
        else:
            ok = False
    print("YES" if ok else "NO")        