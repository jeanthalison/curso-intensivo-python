# -------------------------------------------
# buffet
# -------------------------------------------

buffet = ('frango', 'carne', 'peixe', 'arroz', 'feijão')

print("Itens do buffet:")
for item in buffet:
    print(item)

# Isso vai gerar um erro, pois tuplas são imutáveis
# buffet[0] = 'picanha'

# sobrescrevendo a tupla buffet com novos itens
buffet = ('picanha', 'carne', 'lasanha', 'arroz', 'feijão')

print("\nItens atualizados do buffet:")
for item in buffet:
    print(item)