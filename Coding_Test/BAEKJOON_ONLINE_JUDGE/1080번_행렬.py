N,M = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(N)]
B = [list(map(int, list(input()))) for _ in range(N)]

def flip(x,y,A):
    for i in range(3): # 3x3 행렬을 기준으로 연산을 진행해준다.
        for j in range(3):
            A[x + i][y + j] ^= 1 # XOR 연산 중 0 ^ 1 = 1,  1 ^ 1 = 0 두개를 이용함.

ans = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            flip(i,j,A)
            ans += 1

if A == B:
    print(ans)
else:
    print(-1)
