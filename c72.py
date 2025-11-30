n , l = map(int,input().split())

li = list(map(int,input().split()))
li.sort()

new = []
if n == 1 :
    final = max(li[0] , l-li[0])

else:
    for i in range(1,n):
        new.append(li[i] - li[i-1])


    result = max(new)/2

    distance_to_start = li[0]
    distance_to_end   = l-li[n-1]

    final = max(result,distance_to_end,distance_to_start)
print(f"{final:.10f}")