t = int(input())

for _ in range(t):
    a , b = map(int, input().split())

    final = min(max(2*b,a),max(2*a,b))
    print(final**2)