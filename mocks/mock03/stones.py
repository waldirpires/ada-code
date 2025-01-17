from bisect import insort_left

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort()
        noStonesLeft=0

        while stones:
            heaviest = stones.pop()

            if not stones:
                return heaviest

            nextHeaviest = stones.pop()

            if heaviest > nextHeaviest:
                heavyStones=heaviest-nextHeaviest
                insort_left(stones, heavyStones)

        # no stones were left
        return noStonesLeft

s = Solution()
a = [2,7,4,1,8,1]
r = s.lastStoneWeight(a)
print(r)