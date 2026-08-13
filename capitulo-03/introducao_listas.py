#--------------------------------------------
# lista de bicicletas
#--------------------------------------------

bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
print(bicicletas)

#--------------------------------------------
# acessando elementos de uma lista
#--------------------------------------------

print(bicicletas[0].title())

# sempre devolve a ultima posição
print(bicicletas[-1].title())

#--------------------------------------------
# Usando valores individuais de uma lista
#--------------------------------------------

message = "Minha primeira bicicleta foi " + bicicletas[0].title() + "."
print(message)

# -------------------------------------------
# Modificando elementos de uma lista
# -------------------------------------------

motos = ['honda', 'yamaha', 'suzuki']
print(motos)

motos[0] = 'ducati'
print(motos)

# -------------------------------------------
# Acrescentando elementos a uma lista
# -------------------------------------------

# adiciona no final
motos.append('honda')
print(motos)

# adiciona na determinada posição movendo os itens
motos.insert(0, 'kawasaki')
print(motos)

# -------------------------------------------
# Removendo elementos da lista
# -------------------------------------------

# remove determinado indice
del motos[1]
print(motos)

# removendo com pop()
popped_moto = motos.pop()
print(motos)
print(popped_moto)

# pop() tbm pode remover por indice
primeira_moto = motos.pop(0)
print(motos)
print(primeira_moto)

# removendo de acordo com o valor
print(motos)
motos.remove('suzuki')
print(motos)
