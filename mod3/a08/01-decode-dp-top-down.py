class Solution(object):
    def numDecodings(self, s):
        memo = {}

        def decode_helper(index):
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            if index in memo:
                return memo[index]

            ways = decode_helper(index + 1)
            if index + 1 < len(s) and int(s[index:index+2]) <= 26:
                ways += decode_helper(index + 2)

            memo[index] = ways
            return ways

        return decode_helper(0)

s = Solution()
r = s.numDecodings("12")
print(r)