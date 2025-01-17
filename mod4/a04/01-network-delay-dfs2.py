from collections import defaultdict
import heapq
from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # Common code for all

        graph = defaultdict(list)
        for u, v , w in times:
            graph[u].append((w,v))

        dist = {node: float('inf') for node in range(1,n+1)}

# DFS
        def dfs(node, elapsed):
            if elapsed >= dist[node]: return # Recursion hence base case,
            # If elapsed time > the optimal distance in dist[node]
                #We break
            # If its equal
                # we still break
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                # Why Sorted? --> Does TLE otherwise,
                # It is a greedy Strategy, It is not neccessarily required in DFS

                # To speed things up, at each visited node we'll consider signals exiting the node that are faster first, by sorting the edges.
                dfs(nei, elapsed + time)

        dfs(k, 0)
        ans = max(dist.values())
        #print(dist)
        return ans if ans < float('inf') else -1



# QUEUE

        pq = deque() # Queue
        pq.appendleft((0,k))
        dist = [float('inf') for _ in range(1, n+2)]
        dist[k]=0

        while pq:
            elapsed_time, node = pq.popleft()
            for time, nei in graph[node]:
                    if elapsed_time + time < dist[nei]:
                        dist[nei] = elapsed_time + time
                        pq.appendleft((elapsed_time + time,nei))
        ans = max(dist[1:])
        print(dist)
        return ans if ans < float('inf') else -1

# Dijkstra's Algorithm

        pq = [(0,k)]
        dist = {} # visit all nodes with weight so hashmap works...

        while pq:
            elapsed_time, node = heapq.heappop(pq) # always select shortest weight from graph
            if node not in dist:
                dist[node] = elapsed_time
                for nei, time in graph[node]:
                    if nei not in dist:
                        heapq.heappush(pq,(time + elapsed_time,nei))

        return max(dist.values()) if len(dist) == n else -1