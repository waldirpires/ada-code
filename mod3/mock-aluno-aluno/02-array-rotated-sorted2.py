class Solution():
    def check(self, nums):
        count = 0
        # para cada um dos valores no vetor
        for i in range(len(nums)):
            # se o numero corrente for menor que seu anterior
            cur = nums[i]
            prev = nums[i-1]
            if cur < prev:
                # contabilizar o corte
                count += 1
            # se houver mais de um corte, o vetor sem-cortes não está ordenado
            if count > 1:
                return False
        # encontrado somente um corte
        return True

s = Solution()
nums = [3,4,5,1,2]
r = s.check(nums)
print(r)

# 3 4 5 1 2
# *       *
# 3 4 5 1 2
# * *
# 3 4 5 1 2
#   * *
# 3 4 5 1 2
#     * * = 1 corte
# 3 4 5 1 2
#       * *

# 3 4 5 1 6
# *       * = 1 corte
# 3 4 5 1 6
# * *
# 3 4 5 1 6
#   * *
# 3 4 5 1 6
#     * * = 1 corte
# 3 4 5 1 6
#       * *
# total 2 cortes -> false