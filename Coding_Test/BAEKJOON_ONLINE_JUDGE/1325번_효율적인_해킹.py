from collections import deque

def bfs(i):
    q=deque([i])
    visited=[False]*(n+1)
    visited[i]=True
    count=1
    while q:
        i=q.popleft()
        for e in adj[i]:
            if not visited[e]:
                q.append(e)
                visited[e]=True
                count += 1 
    return count                
                    
n,m=map(int,input().split())
adj=[[] for _ in range(n+1)]

for _ in range(m):
    y,x=map(int,input().split())
    adj[x].append(y)

result=[]
max_value=-1

for i in range(1, n+1):
    count=bfs(i)
    if count > max_value:
        result=[i]
        max_value=count
    elif count == max_value:
        result.append(i)
        max_value=count

for e in result:
    print(e, end=' ')
