## 상,하,좌,우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    global result
    q=set()
    q.add((x,y,array[x][y]))
    
    while q:
        x,y,step=q.pop()
        result=max(result,len(step))
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < r and ny >= 0 and ny < c and array[nx][ny] not in step:
                    q.add((nx,ny,step+array[nx][ny]))

r,c=map(int, input().split())
array=[]

for _ in range(r):
    array.append(input())

result=0
bfs(0,0)
print(result)
