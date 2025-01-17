class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        buy = prices[0] # tentativa da 1a venda
        for sell in prices[1:]: # para cada um dos demais preços
            if sell > buy: # se o valor de venda for maior que o de compra
                profit = max(profit, sell - buy) # calcula o lucro e salva se for maior
            else:
                buy = sell # caso contrário, compramos neste dia e tentamos vender no futuro

        return profit

s = Solution()
prices = [7,1,5,3,6,4]
r = s.maxProfit(prices)
print(r)

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
