t = int(input())

for _ in range(t):
    s = input()
    a_count = 0
    b_count = 0
    
    for i in s:
        if i == 'A':
            a_count+=1
        else:
            b_count+=1
    print("A" if a_count>b_count else "B")            