import collections
import heapq

class Solution:
    def minCostConnectPoints(self, points):
        adj = collections.defaultdict(list)
        N = len(points)
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2,y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])

        visit = set()
        minH = [[0,0]]
        out = 0
        while minH:
            cost,i = heapq.heappop(minH)
            if i in visit:
                continue
            visit.add(i)
            out += cost
            for w,x in adj[i]:
                if x not in visit:
                    heapq.heappush(minH,[w,x])
        return out

s = Solution()
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
r = s.minCostConnectPoints(points)
print(r)