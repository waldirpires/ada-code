def subsets(arr, index, partial):
    if index >= len(arr):
        return [partial]
    else:
        # in: explorando dentro da solução
        inSolutions = subsets(arr, index+1, partial+[arr[index]])
        # out, saindo da tentativa acima e exporando outros caminhos possíveis no nível
        outSolutions = subsets(arr, index+1, partial)
        return inSolutions + outSolutions

# subsets sem repetição
# conjunto, índice e parcial
solutions = subsets([1, 2, 3], 0, [])
for solution in solutions:
    print(solution)