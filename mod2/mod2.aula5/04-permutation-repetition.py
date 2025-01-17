def permutationWithRepetition(n, arr):
  if len(arr)==n:
    print(*arr)
  else:
    for i in range(1, n+1):
      arr.append(i)
      permutationWithRepetition(n, arr)
      arr.pop(-1)

permutationWithRepetition(4, [])