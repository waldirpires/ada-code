class Solution:
    def PredictTheWinner(self, nums):
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        return self.find(0, n - 1, nums, dp) >= 0

    def find(self, i, j, nums, dp):
        # caso base: mesma posição do vetor, retornar score de i
        if i == j:           return nums[i]
        # caso base: valor jah calculado, retornar o valor
        if dp[i][j] != 0:    return dp[i][j]
        # memorização + calculo do max entre a próxima posição para a direita e posição anterior a esquerda
        # recursão
        right = self.find(i + 1, j, nums, dp)
        left = self.find(i, j - 1, nums, dp)
        dp[i][j] = max(nums[i] - right, nums[j] - left)
        # retornar o valor calculado
        return dp[i][j]

s = Solution()
nums = [1,5,2]
r = s.PredictTheWinner(nums)
print(r)