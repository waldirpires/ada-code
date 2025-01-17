def permutation(n, arr):
  if len(arr)==n:
    print(*arr)
  else:
    for i in range(1, n+1):
      if i not in arr: # sem repetição
        arr.append(i)
        permutation(n, arr)
        arr.pop(-1)

# sem repetição
permutation(4, [])
#permutation(8, [])