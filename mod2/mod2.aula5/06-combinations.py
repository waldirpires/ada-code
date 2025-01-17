def combinations(n, k, partial):
  if len(partial)==k: # caso base
    solutions = [partial]
  elif len(partial)==0: # start
    solutions = []
    for i in range(1, n+1):
      solutions += combinations(n, k, [i]) # passo recursivo
  else:
    lastFromPartial = partial[-1] # último valor do parcial
    solutions = []
    for i in range(lastFromPartial+1, n+1):
      solutions += combinations(n, k, partial+[i]) # passo recursivo
  return solutions

# i.e. quatro números de 2 em 2
solutions = combinations(3, 2, [])
#solutions = combinations(5, 3, [])
for solution in solutions:
  print(solution)