from collections import deque
n,k=map(int,input().split())
Max=100001
time_array=[0]*Max

def bfs():
    q=deque([n])
    while q:
        nowPos=q.popleft()
        if nowPos == k:
            return time_array[nowPos]
        
        for nextPos in [nowPos-1,nowPos+1,nowPos*2]:
            if 0<= nextPos < Max and not time_array[nextPos]:
                time_array[nextPos]=time_array[nowPos]+1
                q.append(nextPos)
print(bfs())                
