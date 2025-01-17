class Solution:
    def PredictTheWinner(self, nums):
        n = len(nums)
        return self.find(0, n - 1, nums) >= 0

    def find(self, i, j, nums):
        # caso base: mesma posição do vetor, retornar score de i
        if i == j:           return nums[i]
        # memorização + calculo do max entre a próxima posição para a direita e posição anterior a esquerda
        # recursão
        right = self.find(i + 1, j, nums)
        left = self.find(i, j - 1, nums)
        return max(nums[i] - right, nums[j] - left)

s = Solution()
nums = [1,5,2]
r = s.PredictTheWinner(nums)
print(r)