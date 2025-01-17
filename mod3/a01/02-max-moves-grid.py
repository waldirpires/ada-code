class Solution:
    def maxMoves(self, grid):

        def helper(row,col) :
            # caso base 1: valor negativo ou fora da matriz
            if row < 0 or row >= m or col >= n:
                return 0

            # caso base 2: valor diferente de zero (peso)
            if dp[row][col] != -1:
                return dp[row][col]

            # todas as direções possíveis
            directions = [(row - 1, col + 1), (row, col + 1), (row + 1, col + 1) ]

            # contador de max moves
            max_moves = 0

            # para cada uma das direções
            for x,y in directions :
                # se a posição for válida
                if x>=0 and x < m and (y < n) and grid[x][y] > grid[row][col] :
                    # se houver um peso
                    if dp[x][y] != -1:
                        max_moves = max(max_moves , 1+dp[x][y])
                    # caso contrário, chama recursivamente
                    else :
                        max_moves = max(max_moves , 1+helper(x,y))

            dp[row][col] = max_moves
            return dp[row][col]



        m = len(grid)
        n = len(grid[0])

        ans = 0
        # preenchendo matriz com -1s
        dp = [[-1 for i in range(n)]for j in range(m)]

        dp[m-1][n-1] = 0

        for i in range(m):
            ans = max(ans , helper(i,0))

        return ans

s = Solution()
grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
r = s.maxMoves(grid)
print(r)