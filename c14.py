n = int(input())
color = input()
remove_count = 0
for i in range(len(color)-1):
    if color[i] == color[i+1]:
        remove_count +=1
print(remove_count)        