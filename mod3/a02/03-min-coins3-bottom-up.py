class Solution:
    def min_ignore_none(self, a, b):
        # se a nao estiver calculado ainda, retornar b
        if a is None:
            return b
        # vice-versa
        if b is None:
            return a
        # retornar o mínimo dos dois
        return min(a, b)

    def minimum_coins(self, m, coins):
        # passo 1: inicializar o espaço adicional para armazenamento
        memo = {}
        # caso base: soma 0, 0 moedas
        memo[0] = 0

        # para cada um dos valores de 1 até m
        for i in range(1, m+1):
            # para cada moeda
            for coin in coins:
                # calcula o subproblema
                subproblem = i - coin
                # se for negativo, descartamos
                if subproblem < 0:
                    continue
                # selecionar o mínimo entre um valor já calculado OU do subproblema + 1 moeda
                memo[i] = self.min_ignore_none(memo.get(i), memo.get(subproblem) + 1)

        # retornar a quantidade mínima de moedas para chegar até m
        return memo[i]

s = Solution()
coins = [1, 4, 5]
m = 13
r = s.minimum_coins(m, coins)
print(r)