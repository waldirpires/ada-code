class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       # Versão iterativa
       memo = []
       for i in range(m):
           memo.append( [-1]*n )

       #Ultimas linhas e colunas só têm uma forma de alcançar o final
       for j in range(n):
           memo[m-1][j] = 1
       for i in range(m):
           memo[i][n-1] = 1

       for j in range(n-2, -1, -1):
           for i in range(m-2, -1, -1):
               memo[i][j] = memo[i+1][j] + memo[i][j+1]

       return memo[0][0]

s = Solution()
r = s.uniquePaths(3, 4)
print(r)