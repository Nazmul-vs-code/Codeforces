n = int(input()) 
k = int(input())
advenced = 0
score = []

for i in range(len(score)):
    print("Enter some numbers : " , end="")
    

    if score[i] >= score[k-1] and score[i]>0:
        advenced +=1

print(advenced)        