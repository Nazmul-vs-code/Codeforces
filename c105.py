from math import gcd


y , w = map(int,input().split())

maximum = max(y,w)
side = 7-maximum
probability = (side / 6)

g = gcd(side,6)
print(f"{side//g}/{6//g}")