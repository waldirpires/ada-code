class Solution:
    # O(n^2) time
    # O(1) space
    def maxSubArray(self, nums: List[int]) -> int:
       n = len(nums)
       maxSum = nums[0]
       for start in range(n):
           # acumulando a soma interna para cada índice
           intervalSum = 0
           for end in range(start, n):
               # acumlando para para end
               intervalSum += nums[end]
               # se ele for maior que a maxSum encontrada
               if intervalSum>maxSum:
                   maxSum = intervalSum
       return maxSum

nums = [2, -1, -3, 4, -1, 2, 1, -5 , 4]
s = Solution()
r = s.maxSubArray(nums)
print(r)
