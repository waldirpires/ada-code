class Solution:
    def pd(self, lin, col, memo):
       if memo[lin][col]!=-1: #Step 2 of PD (Search in memo)
           return memo[lin][col]

       #Step 3 of PD (Save in memo)
       if lin==self.m-1 or col==self.n-1:
           memo[lin][col] = 1
       else:
           memo[lin][col] = self.pd(lin+1, col, memo) + self.pd(lin, col+1, memo)


       return memo[lin][col]


    def uniquePaths(self, m, n):
       self.m = m
       self.n = n
       memo = [] #Step 1 of PD (Initialize memo)
       for i in range(m):
           memo.append( [-1]*n )
       return self.pd(0, 0, memo)

s = Solution()
r = s.uniquePaths(3, 4)
print(r)