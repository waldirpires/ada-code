from collections import defaultdict

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        # Create a graph represented as an adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Set to keep track of visited vertices
        visited = set()
        # Stack for DFS traversal
        stack = [source]

        # Perform DFS iteratively using a stack
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    stack.append(neighbor)

        # If destination is not reachable, return False
        return False

s = Solution()
n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
r = s.validPath(n, edges, source, destination)
print(r)