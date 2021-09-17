from collections import deque

n,m=map(int, input().split())
graph=[[] for _ in range(n+1)]

start=10**9
end=1

for _ in range(m):
    x,y,weight_limit=map(int,input().split())
    graph[x].append((y,weight_limit))
    graph[y].append((x,weight_limit))
    start=min(start,weight_limit)
    end=max(end,weight_limit)

start_node, end_node=map(int,input().split())

## 그래프 탐색( 넓이 탐색 알고리즘 이용 )
def bfs(current_weight):
    queue=deque([start_node])
    visited=[False]*(n+1) ## index 1부터 시작하는 걸 사용하기위해 n+1을 곱함.
    while queue:
        x=queue.popleft()
        for y,weight_limit in graph[x]:
            if not visited[y] and current_weight <= weight_limit:
                visited[y]=True
                queue.append(y)
    return visited[end_node]       

result=start ## 시작 중량제한 값
while start <= end:
    mid=(start+end)//2
    if bfs(mid):
        start=mid+1
        result=mid ## 현재 시점의 중량제한 값
    else:
        end=mid-1
print(result)        
