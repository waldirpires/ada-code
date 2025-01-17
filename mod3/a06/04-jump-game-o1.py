class Solution:
    # O(n) time
    # O(1) space
    def canJump(self, nums):
        # se o vetor tiver tamanho 1, ele sempre chega no final
        if len(nums)==1 : return True
        var=0

        # para cada um dos valores exceto o ultimo
        for m in nums[:-1]:
            # compara o salto atual com o salto anterior -1
            var = max(var-1,m)
            # se um zero for encontrado, não é possível chegar até o final
            if var==0 : return False
        # se o var for maior ou igual a 1, ele chegou até o final
        return var>=1

s = Solution()
nums = [2,3,1,1,4]
r = s.canJump(nums)
print(r)
