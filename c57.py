n = int(input())

chessboard = '. '  * n

c = 'C '
li = []
counter = 0

for i in range(n):
    if i % 2 == 0:
        li.append(chessboard)  #print(chessboard)

    else:    
        li.append(c*n)    #print(c *n)
        counter += n
print(counter)
for row in li:
    print(row)            