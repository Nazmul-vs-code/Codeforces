n = int(input())

li = list(map(int,input().split()))
li.sort()
print(" ".join(map(str,li)))