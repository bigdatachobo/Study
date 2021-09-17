# https://programmers.co.kr/learn/courses/30/lessons/72413
import heapq

def dijkstra(graph, start):
    distances = { node: float('inf') for node in graph }
    distances[start] = 0
    q = []
    heapq.heappush(q, (start,distances[start]))

    while q:
        cn, cd = heapq.heappop(q)
        if distances[cn] < cd:
            continue

        for nn, nd in graph[cn].items():
            d = cd + nd
            if d < distances[nn]:
                distances[nn] = d
                heapq.heappush(q, (nn, d))
    return distances

def solution(n, s, a, b, fares):
    graph = { node: {} for node in range(1,n+1) }

    for ns,nd,m in fares:
        graph[ns][nd] = m
        graph[nd][ns] = m

    dist_s = dijkstra(graph, s)

    answer = 100000000
    for k in range(1,n+1):
        dist_k = dijkstra(graph, k)
        answer = min(answer, dist_s[k] + dist_k[a] + dist_k[b])

    return answer
  
'''
n	s	a	b	fares	                                                                                                      result
6	4	6	2	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]	82
7	3	4	1	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]	                                                    14
6	4	5	6	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]	                                18
'''
