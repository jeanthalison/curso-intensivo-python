# -------------------------------------------
# Alterando lista de convidados
# -------------------------------------------

# codigo do exercicio_3_5.py
convidados = ['Carlos', 'costa', 'Roberto']
message = ", convidado para o jantar!\n"
print(
	convidados[0].title() + message +
	convidados[1].title() + message +
	convidados[2].title() + message + "\n"
)

print(convidados[2].title() + ", não podera ir para o jantar\n")
convidados[2] = 'Klen'
print(
	convidados[0].title() + message +
	convidados[1].title() + message +
	convidados[2].title() + message + "\n"
)

# exercicio 3.6
message = ", Encontrei uma mesa maior\n"
print(
	convidados[0].title() + message +
	convidados[1].title() + message +
	convidados[2].title() + message + "\n"
)

# inserindo no começo da lista
convidados.insert(0, 'Levi')
# inserindo no meio da lista
convidados.insert(2, 'Debora')
# inserindo no final da lista
convidados.append('Manu')

message = ", convidado para o jantar!\n"

print(
	convidados[0].title() + message +
	convidados[1].title() + message +
	convidados[2].title() + message +
	convidados[3].title() + message +
	convidados[5].title() + message +
	convidados[4].title() + message + "\n"
)
