class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1  # Base case: empty string is one valid decoding

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                if i + 1 < n and int(s[i:i+2]) <= 26:
                    dp[i] += dp[i + 2]

        return dp[0]

s = Solution()
r = s.numDecodings("12")
print(r)
