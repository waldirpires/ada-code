class Solution():
    def maxProfit(self, prices):

       firstTransaction = [0]*len(prices)
       secondTransaction = [0]*len(prices)


       minUntilNow = prices[0]
       firstTransaction[0] = 0
       for today in range(1, len(prices)):
           sellingToday = max(prices[today] - minUntilNow, 0)
           firstTransaction[today] = max(sellingToday, firstTransaction[today-1])
           minUntilNow = min(minUntilNow, prices[today])


       maxUntilNow = prices[len(prices)-1]
       secondTransaction[len(prices)-1] = 0


       for today in range(len(prices)-2, -1, -1): # n-2 até 0
           buyingToday = max(maxUntilNow - prices[today], 0)
           secondTransaction[today] = max(buyingToday, secondTransaction[today+1])
           maxUntilNow = max(maxUntilNow, prices[today])


       sumBothTransactions = [0]*len(prices)
       for i in range(len(prices)):
           sumBothTransactions[i] = firstTransaction[i] + secondTransaction[i]
       return max(sumBothTransactions)

s = Solution()
prices = [3,3,5,0,0,3,1,4]
r = s.maxProfit(prices)
print(r)