class Solution:
    def generate(self, numRows):
        res = []

        # para cada fila
        for i in range(numRows):
            if i == 0: # se for a 1a fila
                res.append([1])
                continue

            # apendando o 1
            res.append([1])
            # linha anterior
            arr = res[i - 1]
            # caminhando sobre a linha anterior
            for j in range(1, len(arr)):
                # apendando no início do vetor
                res[-1].append(arr[j - 1] + arr[j])
            # apendando o 1 no início
            res[-1].append(1)

        return res

s = Solution()
r = s.generate(5)
for l in r:
    print(l)