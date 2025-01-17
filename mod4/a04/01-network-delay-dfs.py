from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        timeTo = [0] + [float("inf")] * n
        timeTo[k] = 0

        queue = [k]
        while queue:
            u = queue.pop()
            time = timeTo[u]
            for v, w in graph[u]:
                if timeTo[v] > time + w:
                    timeTo[v] = time + w
                    queue.append(v)

        toReturn = max(timeTo)
        return toReturn if toReturn != float("inf") else -1

s = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
r = s.networkDelayTime(times, n, k)
print(r)