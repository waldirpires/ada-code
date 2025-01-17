class Solution:
    def PredictTheWinner(self, nums):
        #@cache
        def gain(start, end):
            # Max gain is you get start and opponent gets max gain of array start+1, end or you get end and opponent gets max gain of array start, end-1
            left = nums[start]-gain(start+1, end)
            right = nums[end]-gain(start, end-1)
            return max(left, right) if start!=end else nums[start]
        return gain(0, len(nums)-1)>=0

s = Solution()
nums = [1,5,2]
r = s.PredictTheWinner(nums)
print(r)