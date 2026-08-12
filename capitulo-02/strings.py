# brincando com Strings

mensagem_1 = "this is a string"
mensagem_2 = 'this is also a string'
mensagem_3 = 'i told my friend, "python is my favorite language!"'

print(mensagem_1)
print(mensagem_2)
print(mensagem_3)


name = "thalison jean"

print(name.title())
print(name.upper())
print(name.lower())


first_name = "thalison"
last_name = "jean"
full_name = first_name + " " + last_name

print("Hello, " + full_name.title() + "!")


mensagem_4 = "Hello, " + full_name.title() + "!"
print(mensagem_4)


print("\t tabulação")
print("\n quebra de linha")

print("language:\n\tpython\n\tc\n\tjava")


favorite_language = ' python '
print(favorite_language + "teste")
print(favorite_language.rstrip() + "teste")
print("teste" + favorite_language.lstrip())
print("teste" + favorite_language.strip() + "teste")
