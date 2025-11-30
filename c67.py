n, m = map(int, input().split())

puzzles = list(map(int, input().split()))
puzzles.sort()
new = []

for i in range(m-n+1):
    new.append(puzzles[i + n-1] - puzzles[i])
print(min(new))    