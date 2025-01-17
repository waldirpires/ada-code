class Solution:
    def topologicalSort(self, edges, n):
        adj = {}
        for i in range (1, n+1):
            adj[i] = []
        for src, dst in edges:
            adj[src].append(dst)

        topSort = []
        visit = set()
        for i in range(1, n+1):
            self.dfs(i, adj, visit, topSort)

        topSort.reverse()
        return topSort()

    def dfs(self, src, adj, visit, topSort):
        if src in visit:
            return
        visit.add(src)

        for neighbor in adj[src]:
            self.dfs(neighbor, adj, visit, topSort)
        topSort.append(src)

s = Solution()
edges = [[3, 2], [3, 5], [2, 6], [5, 1], [6, 4], [1, 4]]
r = s.topologicalSort(edges, 6)
print(r)