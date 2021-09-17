N,M = map(int, input().split())
A = [[ 0 for _ in range(M+1)] for _ in range(N+1)]
DP = [[ 0 for _ in range(M+1)] for _ in range(N+1)]
## DP[i][j] = j,
for i in range(N):
    for j, elem in enumerate(list(map(int, list(input())))):
        A[i+1][j+1] = elem

for i in range(1,N+1):
    for j in range(1,M+1):
        if A[i][j]:
            DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1

print( max([max(i) for i in DP])**2 )
