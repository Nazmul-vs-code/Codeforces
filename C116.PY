
# def prime_check(num):
#     if num <=1:
#         return False
#     for i in range(2,num):
#         if num%i == 0:
#             return False     
#     return True
prims = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]



n , m = map(int, input().split())

index = prims.index(n)

if prims[index] == 47:
    print("NO")
    exit()

if prims[index+1]==m:
    print("YES")
else:
    print("NO")
index = 0        
    
    