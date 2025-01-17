class Solution:
    def minimumTotal(self, triangle):
       memo = dict()
       # filling the last line first (triangle[-1] is the last line)
       row = len(triangle)-1
       for col in range(len(triangle[row])):
           memo[ (row, col) ] = triangle[row][col]
       #filling the lines back to front
       for row in range(len(triangle)-2, -1, -1):
           for col in range(len(triangle[row])):
               memo[(row, col)] = min( memo[(row+1, col)], memo[(row+1, col+1)]) + triangle[row][col]
       return memo[(0,0)]

s = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
r = s.minimumTotal(triangle)
print(r)