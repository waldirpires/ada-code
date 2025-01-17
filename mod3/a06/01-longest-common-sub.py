class Solution:
   def longestCommonSubsequence(self, text1, text2):
       size1 = len(text1)
       size2 = len(text2)
       # criando matriz para memoização
       memo = [ [-1]*(size2+1) for _ in range(size1+1) ]

       # pd
       def pd(size1, size2):
           # caso base: textos vazios
           if size1==0 or size2==0:
               return 0
           # caso base: valor já calculado
           if memo[size1][size2]!=-1:
               return memo[size1][size2]

           # passo recursivo
           # se houver um match, seguir para o caractere anterior
           if text1[size1-1]==text2[size2-1]:
               memo[size1][size2] = 1+pd(size1-1, size2-1)
           else:
               # senão explora dois lados da comparação
               memo[size1][size2] = max(pd(size1-1, size2), pd(size1, size2-1))

           # retorna valor memorizado
           return memo[size1][size2]

       return pd(size1, size2)

s = Solution()
text1 = "abcde"
text2 = "ace"
r = s.longestCommonSubsequence(text1, text2)
print(r)