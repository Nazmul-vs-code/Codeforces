n = int(input())
string = input()
string = string.lower()
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabets = alphabets.lower()

uniq_string = set(string)
result = True

for i in alphabets:
    if i not in uniq_string:
        result = False
        break
if result:
    print("YES")    
else:
    print("NO")    