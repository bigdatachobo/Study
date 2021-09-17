import heapq
import copy

K, N = map(int, input().split())
primes = list(map(int, input().split()))

lst, ck = copy.deepcopy(primes), set()

heapq.heapify(lst)
ith = 0

while ith < N:
    mn = heapq.heappop(lst)
    if mn in ck:
        continue
    ith += 1
    ck.add(mn)
    for i in primes:
        if mn * i <= 2**31:
            heapq.heappush(lst, mn * i)

print(list(ck)[-1])
