class Solution:
    # O(n^3) time
    # O(1) space
    def maxSubArray(self, nums):
       n = len(nums)
       maxSum = nums[0]
       for start in range(n):
           for end in range(start, n):
               intervalSum = 0
               for i in range(start, end+1):
                   intervalSum += nums[i]
               if intervalSum>maxSum:
                   maxSum = intervalSum
       return maxSum

nums = [2, -1, -3, 4, -1, 2, 1, -5 , 4]
s = Solution()
r = s.maxSubArray(nums)
print(r)