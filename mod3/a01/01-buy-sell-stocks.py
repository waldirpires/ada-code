class Solution:
    def maxProfit(self, prices):
        # primeiro preço
        min_price = prices[0]
        
        max_profit = 0

        # para cada um dos demais preços
        for price in prices[1:]:
            # calcular o max profit
            max_profit = max(max_profit, price - min_price)
            # armazenamento o menot preço
            min_price = min(min_price, price)

        return max_profit

s = Solution()
prices = [7,1,5,3,6,4]
r = s.maxProfit(prices)
print(r)