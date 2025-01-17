class Solution(object):
    # O(nlogn) time
    # O(n) space
    def lengthOfLIS(self, nums):
        # step 1: espaço para memoização
        tails = [0] * len(nums)
        size = 0
        # para cada um dos valores
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size

s = Solution()
nums = [10,9,2,5,3,7,101,18]
r = s.lengthOfLIS(nums)
print(r)