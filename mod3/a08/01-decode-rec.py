class Solution(object):
    def numDecodings(self, s):
        def decode_helper(index):
            if index == len(s):
                return 1  # Reached the end, one valid decoding
            if s[index] == '0':
                return 0  # If current digit is '0', it cannot be decoded alone
            ways = decode_helper(index + 1)  # Single-digit decoding
            if index + 1 < len(s) and int(s[index:index+2]) <= 26:
                ways += decode_helper(index + 2)  # Two-digit decoding
            return ways
        return decode_helper(0)

s = Solution()
r = s.numDecodings("12")
print(r)