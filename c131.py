
t = int(input())

for _ in range(t):
    li = []
    for _ in range(10):
        s = input()
        li.append(s)
        
    score = 0
    points = [1,2,3,4,5,5,4,3,2,1]
        
    for i in range(10):
        for j in range(10):
            if li[i][j] == 'X':
                score += min(points[i],points[j])
    print(score)            