class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        # two pointers
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            # se o preço for menor, calcular o max profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else: # caso contrário, continuar comprando
                left = right
            right += 1 # caminhando
        return max_profit # retornar o max profit encontrado

s = Solution()
prices = [7,1,5,3,6,4]
r = s.maxProfit(prices)
print(r)