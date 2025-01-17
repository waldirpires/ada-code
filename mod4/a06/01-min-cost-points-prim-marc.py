import heapq

class Solution:
    def minCostConnectPoints(self, points):
        visited = set()
        heap = [(0, points[0][0], points[0][1])]
        res = 0

        def calc_dist(x1, x2, y1, y2):
            return abs(x1 - y1) + abs(x2 - y2)

        while heap:
            dist, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            res += dist
            for x, y in points:
                if (x, y) in visited:
                    continue

                new_dist = calc_dist(i, j, x, y)
                heapq.heappush(heap, (new_dist, x, y))

        return res


s = Solution()
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
r = s.minCostConnectPoints(points)
print(r)