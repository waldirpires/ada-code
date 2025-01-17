class Solution:
    def pd(self, lin, col):
       if lin==self.m-1 or col==self.n-1:
           return 1
       else:
           return self.pd(lin+1, col) + self.pd(lin, col+1)

    def uniquePaths(self, m, n):
       self.m = m
       self.n = n
       return self.pd(0, 0)

s = Solution()
r = s.uniquePaths(3, 4)
print(r)