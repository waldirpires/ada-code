class Solution:
    def remainingMethods(self, n, k, invocations):
        res, component, g = set(range(n)), set(), defaultdict(set)
        for a, b in invocations: g[a].add(b)
        def dfs(node):
            component.add(node)
            [dfs(to) for to in g[node] if to not in component]
        dfs(k)
        for node in range(n):
            if node not in component and g[node] & component: return res
        return res - component