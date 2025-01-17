class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return amount

        nodeToVisit = []
        visited = set()
        for coin in coins:
            nodeToVisit.append((amount - coin, 1))
            visited.add(amount - coin)

        while nodeToVisit:
            rest, count = nodeToVisit.pop(0)

            if rest == 0:
                return count

            for coin in coins:
                if rest - coin not in visited and rest-coin >= 0:
                    nodeToVisit.append((rest - coin, count + 1))
                    visited.add(rest-coin)

        return -1