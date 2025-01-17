class Solution:
   def pd(self, triangle, row, col, memo=dict()):
       # caso base: ultima linha do triangulo
       if row==len(triangle)-1:
           memo[(row, col)] = triangle[row][col]
           return memo[(row, col)]
       # celula jah visitada
       elif (row, col) in memo:
           return memo[(row, col)]
       else:
           child1 = self.pd(triangle, row+1, col, memo)
           child2 = self.pd(triangle, row+1, col+1, memo)
           memo[(row, col)] = min(child1, child2)+triangle[row][col]
           return memo[(row, col)]


   def minimumTotal(self, triangle):
       return self.pd(triangle, 0, 0, dict())

s = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
r = s.minimumTotal(triangle)
print(r)