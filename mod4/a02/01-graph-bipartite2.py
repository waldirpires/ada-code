class Solution:
    def isBipartite(self, graph):
        parts = [0] * len(graph)
        for i in range(len(graph)):
            if parts[i] != 0:
                continue
            parts[i] = 1
            if not self.dfs(graph, parts, i):
                return False
        return True

    def dfs(self, graph, parts, i):
        for next in graph[i]:
            if parts[next] == 0:
                parts[next] = -parts[i]
                if not self.dfs(graph, parts, next):
                    return False
            elif parts[next] == parts[i]:
                return False
        return True

s = Solution()
g = [[1,2,3],[0,2],[0,1,3],[0,2]]
r = s.isBipartite(g)
print(r)