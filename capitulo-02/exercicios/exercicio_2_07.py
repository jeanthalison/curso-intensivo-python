# manipulando string para tirar espaços em branco com a função strip()

nome = " Thalison "
print(
	"Espaço em branco dos dois lados\n" +
	"\t|" + nome + "|\n" +
	"Removendo espaço em branco do lado direito com rstrip()\n" +
	"\t|" + nome.rstrip() + "|\n" +
	"Removendo espaço em branco do lado esquerdo com lstrip()\n" +
	"\t|" + nome.lstrip() + "|\n" +
	"Removendo espaço em branco dos dois lados com strip()\n" +
	"\t|" + nome.strip() + "|\n"
	)
