class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        if k > len(tickets):
            return 0

        c=0 # initialize counter

        while True: # infinite loop, exit only when kth customer has no tickets to buy
            if tickets[k]==0:    break #if k-th customer has no more tickets to buy, we break the loop
            for i in range(len(tickets)): # for every customer
                if tickets[k]==0:    break # if k-th customer has no more tickets to buy, we break the loop
                if tickets[i]>0: # if there are tickets
                    tickets[i]-=1 # decrement the ticket amount
                    c+=1 # increment counter
        return c # return the counter desired

tickets = [2, 3, 2]
k = 2
s = Solution()
r = s.timeRequiredToBuy(tickets, k)
print(r)