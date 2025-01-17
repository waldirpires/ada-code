class Solution:
    def rob(self, nums):
        a = 0
        b = 0
        for c in nums:
            a, b = b, max(c + a, b)
            print (c, a, b)
        return max(a, b)

s = Solution()
#nums = [1,2,3,1]
nums = [10,1,1,10]
r = s.rob(nums)
print(r)