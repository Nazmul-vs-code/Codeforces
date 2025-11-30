n = int(input())

height = list(map(int,input().split()))
# index = 0

maximum = max(height)
minimum = min(height)
maxindex = height.index(maximum)
rev_shortest_ind = height[::-1].index(minimum)

minindex = len(height)-1-rev_shortest_ind


if maxindex == 0:
    totalswap = n-1-minindex

elif maxindex>minindex:
    totalswap = maxindex + (n-1- minindex) -1

else:    
    totalswap = maxindex + (n-1- minindex) 
print(totalswap)    