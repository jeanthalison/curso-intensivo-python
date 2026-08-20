# -------------------------------------------
# reduzindo lista de convidados
# -------------------------------------------

convidados = ['Carlos', 'Costa', 'Roberto', 'Klen', 'Levi', 'Debora', 'Manu']
message = ", infelizmente, não poderei convidar todos para o jantar, apenas duas pessoas!\n"

# informando que não poderei convidar todos para o jantar
print(
	convidados[0].title() + message +
	convidados[1].title() + message +
    convidados[2].title() + message +
    convidados[3].title() + message +
    convidados[4].title() + message +
    convidados[5].title() + message +
	convidados[6].title() + message +
    "\n"
)

# avisando individualmente que infelizmente não poderei convidar para o jantar
convidado_removido = convidados.pop()
print(convidado_removido.title() + ", infelizmente, não poderei convidar para o jantar!\n")

convidado_removido = convidados.pop()
print(convidado_removido.title() + ", infelizmente, não poderei convidar para o jantar!\n")

convidado_removido = convidados.pop()
print(convidado_removido.title() + ", infelizmente, não poderei convidar para o jantar!\n")

convidado_removido = convidados.pop()
print(convidado_removido.title() + ", infelizmente, não poderei convidar para o jantar!\n")

convidado_removido = convidados.pop()
print(convidado_removido.title() + ", infelizmente, não poderei convidar para o jantar!\n")

# avisando os dois convidados que ainda estão na lista de convidados que ainda estão convidados para o jantar
print(
    convidados[0].title() + ", você ainda está convidado para o jantar!\n" +
    convidados[1].title() + ", você ainda está convidado para o jantar!\n"
)

# lista vazia de convidados
del convidados[0:2]
print(convidados)