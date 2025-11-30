n = int(input())

mishka = 0
chris = 0
for _ in range(n):
    m , c = map(int, input().split())
    if m>c:
        mishka+=1
    if m<c:
        chris+=1    
if mishka>chris:
    print("Mishka")        
elif mishka<chris:
    print("Chris")    
else:
    print("Friendship is magic!^^" )    