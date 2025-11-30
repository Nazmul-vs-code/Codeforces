t = int(input())

for _ in range(t):
    n = int(input())
    new_bin = []
    bin = input().strip()
    
    while len(bin)>1 and bin[0] != bin[-1]:
        bin = bin[1:-1]
    
    print(len(bin))          

