class Solution:
   # TIME:
   # O(4^n * n)
   # 4^n: quantidade de combinações possíveis (4 -> 7, 9)
   # n: tamanho do vetor de dígitos
   #
   # SPACE
   # Espaço auxiliar: depende do tamanho da recursão, pior caso vezes -> O(n)
   # Espaço solução: O(4^n) - todas as combinações possíveis
   def letterCombinations(self, digits):
       if digits=="": # caso base
           return []

       # dicionário para armazenar os valores por dígito (teclado)
       keyboard = dict()
       keyboard["2"] = "abc"
       keyboard["3"] = "def"
       keyboard["4"] = "ghi"
       keyboard["5"] = "jkl"
       keyboard["6"] = "mno"
       keyboard["7"] = "pqrs"
       keyboard["8"] = "tuv"
       keyboard["9"] = "wxyz"

       output = [] # conjunto solução
       if len(digits)==1: # caso base
           for c in keyboard[digits[0]]:
               output.append(c)
       else:
           tailOutput = self.letterCombinations(digits[1:]) # passo recursivo - todos os elementos da posição 1 em diante
           # união das soluções
           for c in keyboard[digits[0]]:
               for tail in tailOutput:
                   output.append(c+tail)
       return output

s = Solution()
solutions = s.letterCombinations("23")
for solution in solutions:
  print(solution)