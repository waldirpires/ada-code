class Solution:
    def modifyString(self, s: str) -> str:
        s = list("0"+s+"0")
        for i, l in enumerate(s[:-1]):
            if l == "?":
                for c in "abc":
                    ant = s[i-1]
                    pos = s[i+1]
                    if c != ant and c != pos:
                        s[i] = c
                        break
        return "".join(s[1:-1])

s = Solution()
str = "?cs"
r = s.modifyString(str)
print(r)
