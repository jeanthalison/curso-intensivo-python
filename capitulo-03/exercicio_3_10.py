# -------------------------------------------
# todas as funções
# -------------------------------------------

linguagens = ['Python', 'C', 'JavaScript', 'Java', 'C#', 'Ruby']

# concatenando com message
message = ", é uma linguagem de programação!\n"
print("Concatenando com message:")
print(
    str(linguagens) + message
)

# modificando um valor
print("\nModificando um valor:")
linguagens[2] = 'R'
print(
    str(linguagens)
)

# inserindo no começo da lista
print("\nInserindo no começo da lista:")
linguagens.insert(0, 'C++')
print(
    str(linguagens)
)

# inserindo no meio da lista
print("\nInserindo no meio da lista:")
linguagens.insert(3, 'PHP')
print(
    str(linguagens)
)

# inserindo no final da lista
print("\nInserindo no final da lista:")
linguagens.append('Go')
print(
    str(linguagens)
)

# removendo um value com pop()
print("\nRemovendo um valor com pop():")
linguagem_removida = linguagens.pop()
print(
    str(linguagens)
)

print("Avisando que a linguagem removida foi: " + linguagem_removida.title())

# removendo um value com del
print("\nRemovendo um valor com del:")
del linguagens[0]
print(
    str(linguagens)
)

# organizando a lista com sort()
print("\nOrganizando a lista com sort():")
linguagens.sort()
print(
    str(linguagens)
)

# tamanho da lista
print("\nTamanho da lista:")
print(
    str(len(linguagens))
)