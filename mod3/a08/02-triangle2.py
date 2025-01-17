class Solution:
    def minimumTotal(self, triangle):

        # Start with bottom-up dynamic programming; this is essentially a dp "triangle"

        # Level-loop
        for level in range( 1, len(triangle) ):

            # First index can only come from first index of the previous
            triangle[level][0] += triangle[level - 1][0]

            # Last index can only come from the last index of the previous
            triangle[level][-1] += triangle[level - 1][-1]

            # Index loop
            for index in range( 1, len(triangle[level]) - 1 ):

                # Find the cheapest way to get there
                right = triangle[level - 1][index]
                left = triangle[level - 1][index - 1]
                triangle[level][index] += min( right, left )

        # Sort the last level and return the minimum (optionally use a last-level min-tracker)
        return sorted( triangle[-1] )[0]


s = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
r = s.minimumTotal(triangle)
print(r)
