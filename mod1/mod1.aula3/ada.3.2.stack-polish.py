
class Solution(object):
    def isOperator(self, s):
        return s in {"+", "-", "*", "/"}

    def evaluate(self, a, b, op):
        if op == "+":
            return b + a
        elif op == "-":
            return b - a
        elif op == "*":
            return b * a
        elif op == "/":
            return int(b / a)
        else:
            return 0

    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if self.isOperator(token):
                a = stack.pop()
                b = stack.pop()
                stack.append(self.evaluate(a, b, token))
            else:
                stack.append(int(token))

        return stack.pop()

# ===================

#a = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
a = ["1"]
s = Solution()
r = s.evalRPN(a)
print(r)