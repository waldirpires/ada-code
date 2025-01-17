class Solution:
    def rob(self, nums):
        def dfs(k):
            # Base Cases
            if k < 0:
                return 0
            # Calculate max money by either robbing current house or skipping it
            return max(dfs(k - 1), dfs(k - 2) + nums[k])

        # Start the recursion from the last house (n - 1)
        return dfs(len(nums) - 1)

s = Solution()
#nums = [1,2,3,1]
nums = [10,1,1,10]
r = s.rob(nums)
print(r)