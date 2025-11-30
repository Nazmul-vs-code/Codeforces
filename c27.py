y = int(input())

y += 1
n = y

while True:
    y_str = str(y)
    if len(set(y_str)) == len(y_str):
        print(y)
        break
    else:
        y+=1
        
