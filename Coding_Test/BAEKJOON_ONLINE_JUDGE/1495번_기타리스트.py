n,s,m=map(int,input().split())
array=list(map(int,input().split()))
dp=[[0]*(m+1) for _ in range(n+1)]

dp[0][s]=1

for num in range(1, n+1):
    for vol in range(m+1):
        if dp[num-1][vol]==0:
            continue
        if vol - array[num-1] >= 0:
            dp[num][vol-array[num-1]]=1
        if vol + array[num-1] <= m:
            dp[num][vol+array[num-1]]=1

result=-1
for vol in range(m,-1,-1):
    if dp[n][vol]==1:
        result=vol
        break
        
print(result)        
