t = int(input())


for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))

    li.sort()

    ok = True

    for i in range(1, n):
        if li[i] - li[i-1] > 1:
            ok = False
            break
    print("YES" if ok else "NO")        