#--------------------------------------------
# Organizando Listas com sort()
#--------------------------------------------

carros = ['bmw', 'audi', 'toyota', 'subaru']
print("Antes do sort(): " + str(carros))

carros.sort()
print("Depois do sort(): " + str(carros))

carros.sort(reverse = True) # inverte a ordem
print("Depois do sort(reverse = True): " + str(carros))

carros = ['bmw', 'audi', 'toyota', 'subaru']
print("\nEstá é a lista original: " + str(carros))
print("Está é usando sorted: " + str(sorted(carros)))
print("Está é a lista original novamente: " + str(carros))

#--------------------------------------------
# Descobrindo tamanho da lista
#--------------------------------------------

print("\nLista de carros: " + str(carros))
print("Tamanho da lista: " + str(len(carros)))
