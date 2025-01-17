def binaryRecursion(n, partial):
  if len(partial)==n:
    print(partial)
  else:
    for c in "01": # variando de 0 a 1
      binaryRecursion(n, partial+c)

binaryRecursion(4, "") # montando uma String
#binaryRecursion(8, "")