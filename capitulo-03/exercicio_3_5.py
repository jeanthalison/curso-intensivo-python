# -------------------------------------------
# Alterando lista de convidados
# -------------------------------------------

# codigo do exercicio_3_4.py
convidados = ['Carlos', 'costa', 'Roberto']
message = ", convidado para o jantar!\n"
print(
	convidados[0].title() + message +
	convidados[1].title() + message +
	convidados[2].title() + message
)

# exercicio 3.5
print(convidados[2].title() + ", não podera ir para o jantar\n")
convidados[2] = 'Klen'
print(
	convidados[0].title() + message +
	convidados[1].title() + message +
	convidados[2].title() + message
)
