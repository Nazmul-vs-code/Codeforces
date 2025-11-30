t = int(input())


for _ in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    
    blank_list = []
    blank_count = 0
    
    for i in li:
        
        
        if i == 0:
            blank_count+=1
        else:
            blank_list.append(blank_count)   
            blank_count = 0 
            
    blank_list.append(blank_count)
    print(max(blank_list))            
