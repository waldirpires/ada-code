def subsets(nums):
    solutions = [] # soluções finais
    partial = [] # solução parcial
    def backtracking(index):
        if index>=len(nums): # caso base
            solutions.append(partial.copy())
        else:
            # in: explorando uma solução parcial interna
            backtracking(index+1)

            partial.append(nums[index])
            # out: backtracking e explorando ums solução externa
            backtracking(index+1)
            partial.pop(-1) # removendo o ultimo elemento
        return solutions
    
    backtracking(0) # start
    return solutions

# subsets que permitem repetição
solutions = subsets([1, 2, 3])
for solution in solutions:
    print(solution)