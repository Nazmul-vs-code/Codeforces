s = input()
word =  "hello" # ['h','e','l','l','o']
index = 0
for i in s:
    if i == word[index]:
        index+=1
        if index == len(word):
            break

if index == len(word):
    print("YES")    
else:
    print("NO")