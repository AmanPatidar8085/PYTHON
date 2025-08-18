def natural(n):
    if(n==1):
        return 1
    return natural(n-1)+n
print (natural(12)) 
