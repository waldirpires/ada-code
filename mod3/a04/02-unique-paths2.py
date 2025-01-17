class Solution:
   def pd(self, grid, row, col, memo):
       rows = len(grid)
       cols = len(grid[0])
       # se passar dos limites OU houver um obstaculo, sair
       if row>=rows or col>=cols or grid[row][col]==1:
           return 0
       # se diferente
       if memo[row][col]!=-1:
           return memo[row][col]
       memo[row][col] = self.pd(grid, row+1, col, memo) + self.pd(grid, row, col+1, memo)
       return memo[row][col]


   def uniquePathsWithObstacles(self, obstacleGrid):
       rows = len(obstacleGrid)
       cols = len(obstacleGrid[0])
       memo = []
       for i in range(rows):
           memo.append( [-1]*cols )
       memo[rows-1][cols-1] = 1
       return self.pd(obstacleGrid, 0, 0, memo)

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
s = Solution()
r = s.uniquePathsWithObstacles(obstacleGrid)
print(r)