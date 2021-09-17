n=int(input())
crane_limits=list(map(int,input().split()))
m=int(input())
box_weights=list(map(int,input().split()))

box_idx=[0]*n
checked=[False]*m

crane_limits.sort(reverse=True)
box_weights.sort(reverse=True)

if max(box_weights) > max(crane_limits):
    print(-1)
else:
    time=0
    box_count=0
    while True:
        if box_count == m:
            break
        for i in range(n):
            while box_idx[i] < m:
                if not checked[box_idx[i]] and crane_limits[i] >= box_weights[box_idx[i]]:
                    checked[box_idx[i]]=True
                    box_count += 1
                    break
                box_idx[i] += 1
        time += 1
    print(time)
