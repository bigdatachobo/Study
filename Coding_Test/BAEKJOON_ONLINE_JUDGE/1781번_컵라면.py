import heapq

n=int(input())
array=[]

for _ in range(n):
    a,b=map(int,input().split())
    array.append((a,b))

array.sort()

q=[]
for deadline,cup in array:
    heapq.heappush(q,cup)
    if deadline < len(q):
        heapq.heappop(q)
print(sum(q))        
