import heapq
n=int(input())
heap=[]
for _ in range(n):
    card_deck=int(input())
    heapq.heappush(heap,card_deck)

result=0    
while len(heap) != 1:
    temp1=heapq.heappop(heap)
    temp2=heapq.heappop(heap)
    sums=temp1+temp2
    result += sums
    heapq.heappush(heap,temp1+temp2)

print(result)    
