# -------------------------------------------
# aprendendo a fatiar uma lista
# -------------------------------------------

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # primeiros 3 jogadores
print(players[1:4])  # jogadores do 2º ao 4º
print(players[:4])   # primeiros 4 jogadores

# pecorrendo uma fatia com laço
print("\nAqui estão os 3 primeiros jogadores da minha lista:")
for player in players[:3]:
    print(player.title())

#copiando uma lista
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]  # copiando a lista inteira

# my_foods = friends_foods {isso nao cria uma copia, apenas criaria uma referencia para a mesma lista, se uma das listas fosse alterada, a outra também seria alterada}

print("\nMinhas comidas favoritas são:")
print(my_foods)

print("\nAs comidas favoritas do meu amigo são:")
print(friends_foods)