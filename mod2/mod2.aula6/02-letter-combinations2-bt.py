class Solution:
    # TIME
    # O(4^n * n)
    # 4^n: quantidade de combinações possíveis (4 -> 7, 9)
    # n: tamanho do vetor de dígitos
    # SPACE
    def letterCombinations(self, digits):
        if digits == "": # caso base
            return []

        hashmap = { # dicionário
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        # backtracking
        def bt(temp_string, i):
            # O(1)
            if len(temp_string) == len(digits): # caso base chegou até o tamanho do vetor
                results.append(temp_string)
                return

            # O(n)
            for j in range(len(hashmap[digits[i]])):
                temp_string += hashmap[digits[i]][j]
                # in
                bt(temp_string, i+1) # vai para o próximo dígito
                # out
                temp_string = temp_string[:-1] #backtrack, retirando o último dígito

        results = [] # conjunto solução
        bt("", 0) # start
        return results

s = Solution()
solutions = s.letterCombinations("235")
for solution in solutions:
  print(solution)