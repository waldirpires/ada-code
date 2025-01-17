class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # caso base
        if numRows == 1:
            return [[1]]

        # passo recursivo para numRows - 1
        prevTriangle = self.generate(numRows-1)
        # pegando a ultima linha para calcular a próxima
        lastRow = prevTriangle[-1]

        newRow = []
        # para cada valor
        for i in range(len(lastRow)-1):
            # calculando os novos elementos da linha
            newRow.append(lastRow[i] + lastRow[i+1])
        # finalizando com os 1s
        newRow = [1] + newRow + [1]
        # retornando o triangulo completo
        return prevTriangle + [newRow]

s = Solution()
r = s.generate(5)
for l in r:
    print(l)