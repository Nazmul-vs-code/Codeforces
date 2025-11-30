k , n , w   = map(int , input().split())

total_cost =0
for i in range(1,w+1):
    total_cost += k*i
    

reminder = total_cost-n 

if reminder<=0:
    print(0)
else:
    print(reminder)