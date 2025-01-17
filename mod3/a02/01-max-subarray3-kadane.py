class Solution:
    # O(n) time
    # O(1) space
    def maxSubArray(self, nums):
       #kadane
       # armazenando o máximo de todos
       max_so_far = nums[0]
       # valor máximo obtido até aquele elemento
       max_ending_here = 0
       # iterando sobre cada um dos valores
       for i in range(len(nums)):
           # acumulando a soma até o elemento corrente
           max_ending_here = max_ending_here + nums[i]
           # se ele ganhar do max_so_far
           if max_so_far < max_ending_here:
               max_so_far = max_ending_here
           # se ele for negativo, ele não contribui, então começamos a acumular do zero e começamos a contar de novo
           if max_ending_here < 0:
               max_ending_here = 0
       return max_so_far

nums = [2, -1, -3, 4, -1, 2, 1, -5 , 4]
s = Solution()
r = s.maxSubArray(nums)
print(r)