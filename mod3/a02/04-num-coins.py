from collections import defaultdict

class Solution:
    def how_many_coins(self, m, coins):
        # dicionário com valor default zero
        # step 1: espaço adicional para armazenamento
        memo = {}
        #= defau

        memo[0] = 1
        # para cada valor até m
        for i in range(1, m+1):
            memo[i] = 0
            # pra cada moeda
            for coin in coins:
                # calcula o subproblema
                subproblem = i - coin
                # se negativo, descarta a moeda
                if subproblem < 0:
                    continue
                # step 2: usar a memoization
                # step 3: salvar a solução parcial ma memoization
                memo[i] += memo[subproblem]

        return memo[m]

s = Solution()
coins = [1, 4, 5]
m = 5
r = s.how_many_coins(m, coins)
print(r)