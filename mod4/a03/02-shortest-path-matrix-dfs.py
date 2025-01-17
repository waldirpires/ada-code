class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]: return -1

        Q = [(0,0,0)]
        grid[0][0]=1
        while Q:
            r,c,l=Q.pop(0)

            if r==c==n-1: return l+1

            if r>0 and grid[r-1][c]==0:
                Q.append((r-1,c,l+1))
                grid[r-1][c]=1
            if r>0 and c+1<n and grid[r-1][c+1]==0:
                Q.append((r-1,c+1,l+1))
                grid[r-1][c+1]=1
            if c+1<n and grid[r][c+1]==0:
                Q.append((r,c+1,l+1))
                grid[r][c+1]=1
            if r+1<n and c+1<n and grid[r+1][c+1]==0:
                Q.append((r+1,c+1,l+1))
                grid[r+1][c+1]=1
            if r+1<n and grid[r+1][c]==0:
                Q.append((r+1,c,l+1))
                grid[r+1][c]=1
            if r+1<n and c>0 and grid[r+1][c-1]==0:
                Q.append((r+1,c-1,l+1))
                grid[r+1][c-1]=1
            if c>0 and grid[r][c-1]==0:
                Q.append((r,c-1,l+1))
                grid[r][c-1]=1
            if r>0 and c>0 and grid[r-1][c-1]==0:
                Q.append((r-1,c-1,l+1))
                grid[r-1][c-1]=1

        return -1

s = Solution()
grid = [[0,0,0],[1,1,0],[1,1,0]]
#[[0,1],[1,0]]
r = s.shortestPathBinaryMatrix(grid)
print(r)