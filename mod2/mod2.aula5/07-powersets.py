def powerSets(arr):
  arr.sort()
  solutions = [] # soluções
  def combinationsNotUnique(arr, index, partial):
    if index>=len(arr): # caso base
      if len(solutions)==0 or solutions[-1]!=partial:
        solutions.append(partial)
    else: # passo recursivo
      #in: explorando soluções internas
      combinationsNotUnique(arr, index+1, partial+[arr[index]])
      #out: backtracking e explorando outras soluções externas
      combinationsNotUnique(arr, index+1, partial)
  combinationsNotUnique(arr, 0, []) # start

  return solutions

# todas as combinações possíveis sem repetição
solutions = powerSets( [1, 2, 2] )
for solution in solutions:
  print(solution)