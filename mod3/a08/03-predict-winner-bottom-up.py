class Solution:
    def PredictTheWinner(self, nums):
        dp = nums.copy()
        n = len(nums)
        for l in range(2, n+1):
            limit = n+1-l
            for i in range(limit):
                left = nums[i+l-1]-dp[i]
                right = nums[i]-dp[i+1]
                dp[i] = max(left, right)

        print(dp)
        return dp[0]>=0

s = Solution()
nums = [1,5,2]
r = s.PredictTheWinner(nums)
print(r)