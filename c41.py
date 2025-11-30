n = int(input())
s1 = "I hate "
s2 = "I love "
s3 = "it "
s4 = "that "
l = []

for i in range(n):
    if i%2 == 0 :
        l.append(s1)
    else:
        l.append(s2)

    if i != n-1:    
        l.append(s4)
l.append(s3)
print("".join(l))