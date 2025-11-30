n = input()

new = ""
for i in n:
    if i.isalpha():
        new += i
new = set(new)
print(len(new))       
