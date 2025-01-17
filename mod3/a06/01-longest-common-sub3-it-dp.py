class Solution:
    def longestCommonSubsequence(self, text1, text2):
        # inicializa vetor
        dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

        text1 = " " + text1
        text2 = " " + text2

        # para cada letra em 1
        for i in range(1, len(text1)):
            # para cada letra em 2
            for j in range(1, len(text2)):
                # se forem iguais, continuar explorando o próximo, salvando em dp
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    # caso contrário, explorar outras possibildiades
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        print(dp)
        # ultima posição terá a solução final
        return dp[-1][-1]

s = Solution()
text1 = "abcde"
text2 = "ace"
r = s.longestCommonSubsequence(text1, text2)
print(r)