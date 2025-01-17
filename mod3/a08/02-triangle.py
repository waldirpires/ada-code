class Solution:
    def minimumTotal(self, triangle):
        def dfs(i, j):
            # se explorarmos todos os elementos
            if i == len(triangle):
                return 0

            cur = triangle[i][j]
            # explorar esquerda na linha de baixo
            lower_left = cur + dfs(i + 1, j)
            # explorar a direita
            lower_right = cur + dfs(i + 1, j + 1)

            # retornar sempre o mínimo depois de explorar cada chamada
            return min(lower_left, lower_right)

        return dfs(0, 0)

s = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
r = s.minimumTotal(triangle)
print(r)
