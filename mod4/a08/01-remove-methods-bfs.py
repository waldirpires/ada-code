class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for u,v in invocations: # directed adj_list
            adj_list[u].append(v)
        visited = set()
        queue = deque([k])
        while queue: # bfs group of nodes called by k
            node = queue.popleft()
            visited.add(node)
            for nei in adj_list[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

        res = set(range(n)) # [0, n)
        for u,v in invocations:
            if u not in visited and v in visited: # if at least one node calls any node in the group from outside
                return res # can't remove the group
        return res - visited # remove the group
    