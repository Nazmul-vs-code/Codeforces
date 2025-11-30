n, k = map(int,input().split())

require_time1 = 1
require_time2 = (240 - k)
new = 0
problems = 0
for i in range(1,n+1):
    if (new + i*5) <= require_time2:
        require_time1 = 5*i
        new+=require_time1
        problems+=1
    else:
        break    

print(problems)    