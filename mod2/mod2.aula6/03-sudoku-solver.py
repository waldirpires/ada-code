class Solution:
   count = 0
   # O(n) tempo
   # O(n) espaço
   def findInvalidsForLineAndColumn(self, lin, col):
        invalid = set() # valores inválidos
        for i in range(9): # 0-8
            invalid.add(board[lin][i]) # valores inválidos para coluna
            invalid.add(board[i][col]) # valores inválidos para linha
        return invalid


   # O(m2) tempo
   # O(m2) espaço
   # m = 3
   def findInvalidsInSubMatrix(self, lin, col):
        invalid = set() # valores inválidos
        # tratando cada subquadrado 3x3
        startLin = 3*(lin//3)
        endLin = startLin+3
        startCol = 3*(col//3)
        endCol = startCol+3
        for i in range(startLin, endLin):
            for j in range(startCol, endCol):
                invalid.add(board[i][j]) # adicionando inválidos
        return invalid


   def backtracking(self, board, lin, col):
       # caso base
       if lin>=9: # se todas as linhas foram visitadas, solução encontrada
           return True

       # se chegou no final da coluna, voltar para 0
       nextCol = col+1 if col<8 else 0
       nextLin = lin+1 if nextCol==0 else lin # próxima linha

       # se já houver valor, BT para a próxima célula
       if board[lin][col]!='.':
           # passo recursivo - demais posições
           # O(m x n) tempo
           return self.backtracking(board, nextLin, nextCol)
       else: # '.'
           # buscando os inválidos para a linha e coluna corrente
           invalid = self.findInvalidsForLineAndColumn(lin, col)

           # tratando cada subquadrado 3x3
           invalid = invalid.union(self.findInvalidsInSubMatrix(lin, col))

           # para todos os valores possíveis
           #O(n) tentativas
           for c in "123456789":
               if c not in invalid: # se achar alguém válido
                   board[lin][col] = c # coloca no board
                   self.count +=1
                   # segue para a próxima posição - IN
                   if(self.backtracking(board, nextLin, nextCol)):
                       return True
                   # caso contrário, backtrack
                   board[lin][col] = '.' # OUT
       # solução não encontrada
       return False


   def solveSudoku(self, board):
       """
       Do not return anything, modify board in-place instead.
       """
       return self.backtracking(board, 0, 0)

s = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solutions = s.solveSudoku(board)
print(solutions)
for solution in board:
    print(solution)
print("count: " + str(s.count))