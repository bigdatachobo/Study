n=int(input())
array=list()
array.append((0,0,0,0))

for i in range(1, n+1):
    square,height,weight=map(int,input().split())
    array.append((i,square,height,weight))

array.sort(key=lambda x: x[3])    
dp=[0]*(n+1)    

for i in range(1,n+1):
    for j in range(0,i):
        if array[i][1] > array[j][1]:
            dp[i]=max(dp[i],dp[j]+array[i][2])

max_value=max(dp)
index=n
result=[]

while index != 0:
    if dp[index]==max_value:
        result.append(array[index][0])
        max_value -= array[index][2]
    index -= 1

result.reverse()
print(len(result))
for i in result:
    print(i)
