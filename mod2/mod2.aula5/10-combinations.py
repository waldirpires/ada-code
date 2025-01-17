class Combinations: # sem repetição

  def bruteForce(self, n, k, vet, output):
      if len(vet)==k: # caso base
          output.append(vet[:])
      else:
          for i in range(1, n+1):
              if len(vet)==0 or i>vet[-1]:
                  vet.append(i)
                  self.bruteForce(n, k, vet, output) # passo recursivo
                  vet.pop(-1) # removendo o ultimo elemento


  def combine(self, n: int, k: int):
      output = []
      self.bruteForce(n, k, [], output)
      return output

comb = Combinations()
# 4 de 3 em 3
solutions = comb.combine(4, 3)
for solution in solutions:
    print(solution)