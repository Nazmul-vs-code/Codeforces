t = int(input())

for _ in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    count_1 = li.count(1)
    count_2 = li.count(2)
  
    sum_li =  sum(li)
    if sum_li %2 != 0 :
        print("NO") 
    elif count_1== 0 and (count_2%2!=0):
        print("NO")           
    else:
        print("YES")    