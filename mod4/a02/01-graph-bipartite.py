from collections import deque

class Solution:
    def isBipartite(self, graph):
        n=len(graph)
        col=[-1]*n
        for i in range(n):
            if col[i]!=-1:
                continue

            q=deque()
            q.append((i,0))
            while q:
                node,color=q.popleft()
                if col[node]==-1:
                    col[node]=color
                    for nx in graph[node]:
                        q.append((nx,color^1))


                if col[node]!=color:
                    return False

        return True

s = Solution()
g = [[1,2,3],[0,2],[0,1,3],[0,2]]
r = s.isBipartite(g)
print(r)