def minimumObstacles(self, grid: List[List[int]]) -> int:
    #find the min cost path from (0,0) to (m-1, n-1)
    m = len(grid); n = len(grid[0])

    heap = [[grid[0][0], 0, 0]]
    visited = [[0]*n for _ in range(m)]
    visited[0][0] = 1
    while heap:
        c_cost, c_i, c_j = heappop(heap)
        if (c_i,c_j) == (m-1,n-1):
            return c_cost
        for n_i,n_j in [[c_i-1,c_j], [c_i,c_j+1], [c_i+1,c_j], [c_i,c_j-1]]:
            if 0<=n_i<m and 0<=n_j<n and not visited[n_i][n_j]:
                visited[n_i][n_j] = 1
                heappush(heap, [c_cost + grid[n_i][n_j], n_i, n_j])

    return -1