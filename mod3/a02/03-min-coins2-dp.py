class Solution:
    def min_ignore_none(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        return min(a, b)

    # step 1: memória auxiliar para salvar soluções parciais
    memo = {}

    # O(m x k) time -> m= target sum, k=number of coins
    # O(m) space
    def minimum_coins(self, m, coins):
        # step 2: checar memoization
        if m in self.memo:
            return self.memo[m]
        if m == 0:
            return 0

        answer = None
        for coin in coins:
            subproblem = m - coin
            if subproblem < 0:
                continue
            answer = self.min_ignore_none(answer, self.minimum_coins(subproblem, coins) + 1)
        # step 3: salvar solução parcial ma memoization
        self.memo[m] = answer
        return answer

s = Solution()
coins = [1, 4, 5]
m = 13
r = s.minimum_coins(m, coins)
print(r)