m, n = map(int, input().split())


def max_dominos(m , n ):

    if(1<=m<=n<=16):
        dominos = (m*n)/2
        print(int(dominos))

    else:
        print("Please follow the roles (1<=m<=n<=16)")    

max_dominos(m , n)    