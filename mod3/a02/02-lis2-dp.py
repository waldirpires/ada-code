class Solution:
    def LISWithStartingIndex(self, nums, index, memo):
       #Step 2 of PD Searching in memo
       if index in memo:
           return memo[index]
       #starts with nums[index], size 1
       maxSize = 1
       for i in range(index+1, len(nums)):
           if nums[i]>nums[index]:
               size = self.LISWithStartingIndex(nums, i, memo) + 1
               maxSize = max(maxSize, size)
       #Step 3 of PD: Saving in memo
       memo[index] = maxSize
       return maxSize

    def lengthOfLIS(self, nums):
       #Step 1 of PD: Creating memo
       memo = dict()
       maxSize = 0
       for i in range( len(nums) ):
           size = self.LISWithStartingIndex(nums, i, memo)
           maxSize = max(maxSize, size)
       return maxSize

s = Solution()
nums = [10,9,2,5,3,7,101,18]
r = s.lengthOfLIS(nums)
print(r)

