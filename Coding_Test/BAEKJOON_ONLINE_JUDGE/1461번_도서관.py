import heapq
n,m=map(int,input().split())
books=list(map(int,input().split(' ')))
plus=[]
minus=[]

longest=max(max(books),-min(books))

for i in books:
    if i>0:
        heapq.heappush(plus,-i)
    else:
        heapq.heappush(minus,i)

result=0
while plus:
    result += heapq.heappop(plus)
    for _ in range(m-1):
        if plus:
            heapq.heappop(plus)

while minus:
    result += heapq.heappop(minus)
    for _ in range(m-1):
        if minus:
            heapq.heappop(minus)
                
hap=(-result*2)-longest
print(hap)                
