class Solution:
    def findCenter(self, edges):
        n = len(edges)+1
        # memória para o calculo dos graus
        degree = [0]*(n+1)

        # para cada aresta
        for u,v in edges:
            degree[u]+=1
            degree[v]+=1
            # se encontrarmos um vertice de grau n-1, ele é o centro
            if degree[u]==n-1:
                ans = u
            # se encontrarmos um vertice de grau n-1, ele é o centro
            elif degree[v]==n-1:
                ans = v

        return ans

edges = [[1,2],[2,3],[4,2]]
s = Solution()
r = s.findCenter(edges)
print(r)