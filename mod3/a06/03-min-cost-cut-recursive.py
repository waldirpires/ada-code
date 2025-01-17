class Solution:
    def minCostTab(self, n: int, cuts):
        cuts.sort()
        A = [0] + cuts + [n]
        dp = [[0 for j in range(len(cuts)+2)] for i in range(len(cuts)+2)]

        for i in range(len(cuts), 0, -1):
            for j in range(1, len(cuts)+1):
                if i > j:
                    continue
                mini = float("inf")
                for k in range(i, j+1):
                    cost = A[j+1]-A[i-1] + dp[i][k-1] + dp[k+1][j]
                    mini = min(cost, mini)
                dp[i][j] = mini
        return dp[1][len(cuts)]

