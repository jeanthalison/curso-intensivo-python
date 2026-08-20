# -------------------------------------------
# minhas pizzas, suas pizzas
# -------------------------------------------

my_pizzas = ['mussarela', 'calabresa', 'portuguesa']
friend_pizzas = my_pizzas[:]  # copiando a lista inteira

# adicionando uma nova pizza
my_pizzas.append('frango com catupiry')
friend_pizzas.append('marguerita')

print("Minhas pizzas favoritas são:")
for pizza in my_pizzas:
    print(pizza.title())

print("\nAs pizzas favoritas do meu amigo são:")
for pizza in friend_pizzas:
    print(pizza.title())