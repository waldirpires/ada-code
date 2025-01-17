class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0

        c = nums[0]
        mx = nums[0]

        for i in range(1, len(nums)):
            c = max(nums[i], c + nums[i])
            mx = max(mx, c)

        return mx


nums = [2, -1, -3, 4, -1, 2, 1, -5 , 4]
s = Solution()
r = s.maxSubArray(nums)
print(r)