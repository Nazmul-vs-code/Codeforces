n , t = map(int,input().split())
s = input()
sl = list(s)

for l in range(t):
    i = 0
    while i < len(s)-1:
        if sl[i] == "B" and sl[i+1] == 'G':
            sl[i] , sl[i+1] = sl[i+1] , sl[i]
            i += 2
        else:
            i+=1    
final = "".join(sl)
print(final)            