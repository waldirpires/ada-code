class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs_recursive(i, j):
            # caso base: se ambas strings forem vazias
            if i == 0 or j == 0:
                return 0

            # caso base: se os caracteres forem iguais, continuar explorando com o anterior (próximo)
            if text1[i - 1] == text2[j - 1]:
                return 1 + lcs_recursive(i - 1, j - 1)

            # caso contrário, explorar outras possibilidades
            return max(lcs_recursive(i - 1, j), lcs_recursive(i, j - 1))

        m, n = len(text1), len(text2)
        return lcs_recursive(m, n)

s = Solution()
text1 = "aabcde"
text2 = "aace"
r = s.longestCommonSubsequence(text1, text2)
print(r)