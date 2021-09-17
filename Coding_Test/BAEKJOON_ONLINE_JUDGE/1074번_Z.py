N,r,c = map(int, input().split())

def Z(a,x,y):
    if a == 1:
        return 0
    
    a //= 2
    for i in range(2):
        for j in range(2):
            if x < a*(i+1) and y < a*(j+1):
                return (i*2 + j)*(a * a) + Z(a, x - a*i,y - a*j)

print(Z(2**N,r,c))            
