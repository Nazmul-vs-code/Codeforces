word = input()

lower = 0
upper = 0 
for i in word:
    if i.islower():
        lower+=1
    elif i.isupper():
        upper+=1

if upper>lower:
    word = word.upper()
elif upper<lower:
    word = word.lower() 
else:
    word = word.lower()    


print(word)