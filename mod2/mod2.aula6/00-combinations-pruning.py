def combinations(n, k, partial=[]):
    # print(*partial)
    if len(partial)==k:
        print(*partial) # unpack operator
    else:
        # ponto de início: ultima posição + 1
        start = 1 if len(partial)==0 else partial[len(partial)-1]+1
        # para cada um dos valores no intervalo
        for i in range(start, n+1):
            # quantidade de valores disponíveis para processamento
            avaialableNumbers = n+1-i
            # se o tamanho do partial + available numbers for menor que o limite
            # pruning (podagem)
            if len(partial)+avaialableNumbers < k : break
            # adicionar solução parcial
            partial.append(i) # [1]
            # chamada recursiva para explorar a dentro
            combinations(n, k, partial) # backtracking - IN
            partial.pop() # backtracking - OUT

combinations(4, 2) # start

#  n  k  partial
# (4, 2, [])
# [1 2 3 4]
