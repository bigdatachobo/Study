n=int(input())
k=int(input())

if k >= n:
    print(0)
else:    
    sensors=list(map(int,input().split(' ')))
    sensors.sort()

    gap=[]
    for i in range(1,n):
        interval=sensors[i]-sensors[i-1]
        gap.append(interval)
    
    gap.sort(reverse=True)

    for i in range(k-1):
        gap[i]=0

    print(sum(gap))    
