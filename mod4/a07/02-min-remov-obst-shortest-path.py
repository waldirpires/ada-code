class Solution(object):
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])  # Dimensions of the grid
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        visited = [[False] * n for _ in range(m)]  # Visited array

        # Priority queue to store (cost, x, y)
        pq = [(grid[0][0], 0, 0)]  # Start from (0, 0) with its cost
        visited[0][0] = True

        while pq:
            cost, x, y = heappop(pq)

            # If we reach the bottom-right corner, return the cost
            if x == m - 1 and y == n - 1:
                return cost

            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heappush(pq, (cost + grid[nx][ny], nx, ny))

        return -1  # If no valid path exists (unlikely for a valid grid)