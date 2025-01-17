class Solution:
   def isTwoNumberCode(self, s, index):
       if index+1>=len(s):
           return False
       if s[index]=='1' or (s[index]=='2' and ord(s[index+1])-ord('0')<7):
           return True
       return False


   def numDecodings(self, s):
       memo = [0]*len(s)
       
       for i in range(len(s)-1, -1, -1):
           if s[i]=='0':
               memo[i] = 0
           elif self.isTwoNumberCode(s, i):
               if i+2<len(s):
                   memo[i] = memo[i+1] + memo[i+2]
               else:
                   memo[i] = memo[i+1] + 1
           else:
               memo[i] = memo[i+1] if i+1<len(s) else 1
       return memo[0]

s = Solution()
r = s.numDecodings("12")
print(r)