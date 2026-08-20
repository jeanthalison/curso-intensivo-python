# -------------------------------------------
# aprendendo sobre tuplas
# -------------------------------------------

# tuplas sao valores imutaveis, ou seja, não podem ser alterados depois de criados
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# tentando alterar o valor de uma tupla gera um erro
# dimensions[0] = 250  # TypeError: 'tuple' object does not support item assignment

# pecorrendo valores de uma tupla com um laço for
print("\nPercorrendo valores de uma tupla:")
for dimension in dimensions:
    print(dimension)

# sobrescrevendo uma tupla, ou seja, criando uma nova tupla com novos valores, sobescrever uma tupla não é o mesmo que alterar uma tupla
dimensions = (400, 100)
print("\nDimensões atualizadas:")
for dimension in dimensions:
    print(dimension)