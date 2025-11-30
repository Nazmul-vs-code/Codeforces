# print(4%2, 9%2, 2%2, 1%2, 18%2, 3%2, 0%2)  = print(0%2,1%2,2%2,3%2,4%2,5%2,6%2)
# 0 1 0 1 0 1 0 = 0 1 0 1 0 1 0

# print(3%2,2%2,7%2,6%2)
# print(0%2,1%2,2%2,3%2)

t = int(input())

for _ in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    counter_even = 0
    counter_odd = 0
    
    for i in range(n):
        if i%2 != li[i]%2:
            if i%2 == 0:
                counter_even += 1
            else:
                counter_odd += 1
    print(counter_even if  counter_even == counter_odd else -1)            