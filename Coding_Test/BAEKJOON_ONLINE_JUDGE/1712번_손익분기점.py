A, B, C=map(int, input().split())

if B<C:
    x=int(A/(C-B))
    print(x+1)
else:
    print(-1)
