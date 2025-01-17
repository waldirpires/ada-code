class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1=len(word1)
        l2=len(word2)
        # memorização
        dp=[[0]*(l2+1) for i in range(l1+1)]
        cnt=0
        # para cada letra em 1
        for i in range(l1+1):
            # para cada letra em 2
            for j in range(l2+1):
                # caso base
                if i==0:
                    dp[i][j]=j
                elif j==0:
                    dp[i][j]=i
                # se as letras forem iguais, segue explorando
                elif word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    # se forem diferentes, pegar o mínimo de três possibilidades
                    dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
        print(dp)
        return dp[-1][-1]

s = Solution()
word1 = "aba"
word2 = "aca"
# [[0, 1, 2, 3],
#  [1, 0, 1, 2],
#  [2, 1, 1, 2],
#  [3, 2, 2, 1]]
r = s.minDistance(word1, word2)
print(r)