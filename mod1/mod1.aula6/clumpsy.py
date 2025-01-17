def clumsy_factorial(n):
    # caso base para valores abaixo de 4
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2 * 1
    elif n == 3:
        return 3 * 2 // 1

    # aplicar a 1a parte
    result = n * (n-1) // (n-2) + (n-3)

    # aplicar a 2a parte e calcular o clumsy da subtração
    return result - clumsy_factorial(n-4)

print(clumsy_factorial(8))
print(clumsy_factorial(10))