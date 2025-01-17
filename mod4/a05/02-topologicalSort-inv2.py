class Solution:
    def topologicalSort(self, edges, n):
        # criando a lista de adjacentes
        adj = {}
        for i in range (1, n+1):
            adj[i] = []
        for src, dst in edges:
            adj[src].append(dst)

        topSort = []
        visit = set()
        paths = set()
        # utilizando o DFS para processar os caminhos
        for i in range(1, n+1):
            # caso in ciclo seja encontrado, não é possível ordenar
            if self.dfs(i, adj, visit, paths, topSort):
                return []

        # invertendo a lista
        topSort.reverse()
        return topSort

    def dfs(self, src, adj, visit, paths, topSort):
        if self in paths:
            return False

        if src in visit:
            return

        paths.add(src)
        visit.add(src)

        for neighbor in adj[src]:
            isAcyclic = self.dfs(neighbor, adj, visit, paths, topSort)
            if isAcyclic == False:
                return False

        topSort.append(src)
        paths.remove(src)

s = Solution()
edges = [[3, 2], [3, 5], [2, 6], [5, 1], [6, 4], [1, 4]]
r = s.topologicalSort(edges, 6)
print(r)