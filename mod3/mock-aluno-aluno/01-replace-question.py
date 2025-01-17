class Solution:
    def modifyString(self, s):
        if len(s)==1:  #if input contains only a '?'
            if s[0]=='?':
                return 'a'
        s=list(s)
        for i in range(len(s)): # para cada uma das letras na String
            if s[i]=='?': # se o coringa for encontrada
                for c in 'abc': # três caracteres consecutivos para substituição
                    if i==0 and s[i+1]!=c: #if i=0 means it is first letter so there is no s[ i-1]
                        s[i]=c
                        break
                    if i==len(s)-1 and s[i-1]!=c: #if i=len(s) means it is last letter so there is no s[i+1]
                        s[i]=c
                        break
                    ant = s[i-1]
                    pos = s[i+1]
                    if (i>0 and i<len(s)-1) and ant!=c and pos!=c:
                        s[i]=c
                        break
        return ''.join(s)

s = Solution()
str = "?cs"
r = s.modifyString(str)
print(r)

# "?cs"
# "?cs"
#  *