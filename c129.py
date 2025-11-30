t = int(input())

for _ in range(t):
    x = int(input())
    x = str(x)
    d = int(x[0])
    le = len(x)
    result = (d-1)*10 + (le*(le+1)//2)
    print(result)