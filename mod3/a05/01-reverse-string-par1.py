class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        ret = ""

        for letter in s:
            if letter == "(":
                stack.append(letter)
            elif letter == ")":
                # is a closing bracket, reverse the string inside
                reversedString = []
                while stack[-1] != "(":
                    topElement = stack.pop()
                    reversedString.append(topElement)
                # at this point, the top element is the matching closing bracket (
                stack.pop() # remove the closing
                if not stack:
                    ret += "".join(reversedString)
                else:
                    stack += reversedString
            else:
                # is a character
                if stack:
                    stack.append(letter)
                else:
                    ret += letter
        return ret

s = Solution()
r = s.reverseParentheses("(abcd)")
print(r)