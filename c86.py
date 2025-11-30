st = input()
li = []
 
i = 0
while i < len(st):
    if st[i] == ".":
        li.append("0")
        i+=1
    elif i+1<len(st) and st[i] == "-" and st[i+1] == ".":
        li.append("1")
        i+=2    
    elif i+1<len(st) and st[i] == "-" and st[i+1] == "-" :
        li.append("2")
        i +=2    
print("".join(li))        