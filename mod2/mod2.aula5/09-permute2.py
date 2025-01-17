class Permutations:

   def permute(self, nums):
       solutions = [] # conjunto total de soluções
       partial = [] # solução parcial

       def backtracking(index: int):
           if index>=len(nums): # caso base
               solutions.append(partial.copy())
           else:
               for num in nums:
                   if num not in partial: # se o numero não estiver ainda no parcial
                       partial.append(num) # adiciona ele
                       backtracking(index+1) #exploro index +1
                       partial.pop(-1) # faço o backtrack, saio e dou sequencia

       backtracking(0)
       return solutions

    # def permute(self, nums) :
    #     solutions = []
    #     partialSet = set() # usando SET

    #     def backtracking(index: int, partial):
    #         if index>=len(nums):
    #             solutions.append(partial)
    #         else:
    #             for num in nums:
    #                 if num not in partialSet:
    #                     partialSet.add(num)
    #                     backtracking(index+1, partial + [num])
    #                     partialSet.remove(num)

    #     backtracking(0, [])
    #     return solutions

perm = Permutations()
solutions = perm.permute([1, 2, 3])
for solution in solutions:
  print(solution)