import heapq
from collections import defaultdict

# Dijkstra
# Time: O((V + E) * log(E))
# Space: O(V+E)
class Solution:
    def networkDelayTime(self, times, n, k):
        visited = set()
        heap = []
        heapq.heappush(heap,[0,k])
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        while heap:
            wei,node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited)==n:
                return wei

            for nei,w in graph[node]:
                heapq.heappush(heap,[w+wei,nei])

        return -1

s = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
r = s.networkDelayTime(times, n, k)
print(r)