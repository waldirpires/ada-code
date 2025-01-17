class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        #
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        # primeiro salto, x, y, quantidade
        q = [(0, 0, 1)]
        # marcar o 1o no como visitado
        grid[0][0] = 1
        for i, j, d in q:
            # se chegarmos no fim, retornar a quantidade de nós
            if i == n-1 and j == n-1: return d
            # para cada um dos movimentos possíveis
            for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                # enquanto x e y estiver dentro da matrix e o nó ainda não estiver sido visitado
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    # marcar a celula
                    grid[x][y] = 1
                    # anexar o caminho
                    q.append((x, y, d+1))
        return -1

s = Solution()
grid = [[0,0,0],[1,1,0],[1,1,0]]
#[[0,1],[1,0]]
r = s.shortestPathBinaryMatrix(grid)
print(r)