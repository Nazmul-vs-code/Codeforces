word = input()
voel = ['a','e','i','o','u','y']
word = word.lower()
result = ""
new = ""
for ch in word:
    if ch not in voel:
        result+=ch

for i in result:
    new +='.'+i 

    
    
print(new)        