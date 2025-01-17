class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        edges = []
        for i in range(n):
            xi, yi = points[i]
            for j in range(i+1, n):
                xj, yj = points[j]
                manhattan = abs(xi-xj)+abs(yi-yj)
                edges.append((manhattan, i, j))
        edges.sort()
        parent = {i: i for i in range(n)}
        depth = {i: 1 for i in range(n)}
        def find(x):
            if parent[x]==x:
                return x
            return find(parent[x])
        def union(x,y):
            if depth[find(x)]>depth[find(y)]:
                parent[find(y)] = find(x)
            elif depth[find(y)]>depth[find(x)]:
                parent[find(x)] = find(y)
            else:
                parent[find(y)] = find(x)
                depth[find(x)] += 1
        mst, cost = 1, 0
        for edge in edges:
            dist, u, v = edge
            if find(u)!=find(v):
                union(u, v)
                cost += dist
                mst += 1
                if mst==n:
                    break
        return cost

s = Solution()
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
r = s.minCostConnectPoints(points)
print(r)
