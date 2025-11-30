n = int(input())

def emnei(n):
    if n < 0:
        new_n = str(n)
        last = new_n[-1]
        second_last = new_n[-2]
        if last > second_last:
            new_n = new_n[:-1]
        else:
            new_n = new_n[:-2] + last
        print(int(new_n))        
    else:
        print(n)    
emnei(n)        