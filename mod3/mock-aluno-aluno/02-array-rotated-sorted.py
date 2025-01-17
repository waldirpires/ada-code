class Solution:
    def check(self, nums):
        count = 0
        l = len(nums)

        # para cada valor no vetor
        for i in range(1,l):
            # se o anterior for maior que o corrente
            if nums[i-1] > nums[i]:
                # contabilizar a contagem de rotações
                count += 1

        # se houve pelo menos duas rotações OU
        # houve uma rotação e primeiro é menor que último
        if count > 1 or (count == 1 and nums[0] < nums[-1]):
            return False
        return True

# 2 4 6 8 10 12
# 10 12 2 4 6 8

s = Solution()
nums = [5, 4, 3]
r = s.check(nums)
print(r)