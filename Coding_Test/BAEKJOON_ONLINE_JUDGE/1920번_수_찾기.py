N = int(input())
A=dict()
temp = list(map(int, input().split()))
for i in temp:
    if not i in A:
        A[i] = 0
    A[i] = 1

M = int(input())
B = list(map(int, input().split()))

for j in B:
    try:
        if A[j]:
            print(A[j])
    except:
        print(0)
