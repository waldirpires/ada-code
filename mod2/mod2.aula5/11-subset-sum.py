import itertools

array = [-3, -2, -1, 0, 0, 1, 2, 3]

for r in range(0, 4):
    unique_permutations = list(set(itertools.combinations(array, r)))
    # To print all unique permutations:
    for perm in unique_permutations:
        total_sum = sum(perm)
        if total_sum in array and len(perm) == 3:
            print(perm)
