# -------------------------------------------
# usando a função range()
# -------------------------------------------

# começa de 1 ate 4 (5 não é incluído)
for value in range(1, 5):
    print(value)

# usando list com range
numbers = list(range(1, 6))
print("\nNúmeros: " + str(numbers))

# usando range com intervalo
# leitura de 2 em 2, começando de 2 até 10 (11 não é incluído)
even_numbers = list(range(2, 11, 2))
print("\nNúmeros pares: " + str(even_numbers))

# quadrados perfeitos de 1 a 10
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print("\nQuadrados perfeitos: " + str(squares))

# estatisticas simples com min(), max() e sum()
list_numbers = list(range(0, 10))
print("\nNúmeros: " + str(list_numbers))
print("Mínimo: " + str(min(list_numbers)))
print("Máximo: " + str(max(list_numbers)))
print("Soma: " + str(sum(list_numbers)))

# usando list comprehension para criar uma lista de quadrados perfeitos
squares_comp = [value ** 2 for value in range(1, 11)]
print("\nQuadrados perfeitos (list comprehension): " + str(squares_comp))