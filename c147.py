from doctest import master


t = int(input())

for _ in range(t):
    s1,s2,s3,s4 = map(int, input().split())
    list1 = [s1,s2]
    list2 = [s3,s4]
    
    if max(list1) < min(list2) or max(list2) < min(list1):
        print("NO")
    else:
        print("YES")    