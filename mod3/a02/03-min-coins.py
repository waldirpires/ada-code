class Solution:
    def min_ignore_none(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        return min(a, b)

    def minimum_coins(self, m, coins):
        if m == 0:
            return 0

        answer = None
        for coin in coins:
            # calcula o subproblema
            subproblem = m - coin
            # se o valor for negativo, descarta o subproblema
            if subproblem < 0:
                continue
            # obtem o mínimo comparando o atual com o subproblema
            answer = self.min_ignore_none(answer, self.minimum_coins(subproblem, coins) + 1)

        # pode não haver resposta
        return answer

s = Solution()
coins = [1, 4, 5]
m = 13
r = s.minimum_coins(m, coins)
print(r)