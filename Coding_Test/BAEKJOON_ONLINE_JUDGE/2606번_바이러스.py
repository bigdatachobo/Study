from collections import deque
n=int(input())
m=int(input())
adj=[[] for _ in range(n+1)]
start_node=1

for _ in range(m):
    x,y=map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

visited=[False]*(n+1)    
count=0

def bfs():
    global count
    q=deque([start_node])
    while q:
        node=q.popleft()
        if not(visited[node]):
            visited[node]=True
            count += 1
            for element in adj[node]:
                if not(visited[element]):
                    q.append(element)
bfs()
print(count-1)                    
