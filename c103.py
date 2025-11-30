t = int(input())

for i in range(t):
    a , b = map(str,input().split())
    c = f"{b[0]}{a[1:]}"
    d = f"{a[0]}{b[1:]}"
    print(f"{c} {d}")