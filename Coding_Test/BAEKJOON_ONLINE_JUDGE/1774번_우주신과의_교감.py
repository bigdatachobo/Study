import math
import sys
input=sys.stdin.readline

def get_distance(a,b):
    x=a[0]-b[0]
    y=a[1]-b[1]
    length=math.sqrt((x*x)+(y*y))
    return length

def find(parent,n):
    if parent[n]==n:
        return n
    return find(parent,parent[n])

def make_set(parent,n):
    parent[n]=n
    rank[n]=0

def union(parent,a,b):
    root1=find(parent,a)
    root2=find(parent,b)
    if rank[root1] > rank[root2]:
        parent[root2]=root1
    else:
        parent[root1]=root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

n,m=map(int,input().split())            
edges=list()
points=list()
parent=dict()
rank=dict()

for _ in range(n):
    x,y=map(int,input().split())
    points.append((x,y))
    
count=len(points)

for i in range(count-1):
    for j in range(i+1,count):
        edges.append((i+1,j+1,get_distance(points[i],points[j])))

for i in range(1,n+1):
    make_set(parent,i)

for _ in range(m):
    a,b=map(int,input().split())
    union(parent,a,b)

edges.sort(key=lambda x: x[2])

result=0
for edge in edges:
    nodeA,nodeB,cost=edge
    if find(parent,nodeA) != find(parent,nodeB):
        union(parent,nodeA,nodeB)
        result += cost
print("%0.2f" % result)        
