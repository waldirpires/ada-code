class Solution:
    def LISWithStartingIndex(self, nums, index):
       #initialize with size 1, that it is just nums[index]
       maxSize = 1
       for i in range(index+1, len(nums)):
           if nums[i]>nums[index]:
               size = 1 + self.LISWithStartingIndex(nums, i)
               #this subsequence starts with num[index] + lis of index i
               maxSize = max(maxSize, size) #keeping the longest
       return maxSize

    def lengthOfLIS(self, nums):
       maxSize = 0
       for i in range( len(nums) ): #trying to start in all indexes
           size = self.LISWithStartingIndex(nums, i)
           maxSize = max(maxSize, size) #keeping the longest
       return maxSize

s = Solution()
nums = [10,9,2,5,3,7,101,18]
r = s.lengthOfLIS(nums)
print(r)