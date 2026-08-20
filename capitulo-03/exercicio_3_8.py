# -------------------------------------------
# conhecendo o mundo
# -------------------------------------------

lugares = ['canada', 'frança', 'portugal', 'italia', 'japão']

print("Lista original: " + str(lugares))
print("Lista ordenada (sem modificar a lista original): " + str(sorted(lugares)))
print("Lista ordenada de forma reversa (sem modificar a lista original): " + str(sorted(lugares, reverse=True)))

lugares.reverse()
print("Lista reversa (modificando a lista original): " + str(lugares))

lugares.reverse()
print("Lista reversa (modificando a lista original): " + str(lugares))

lugares.sort()
print("Lista ordenada (modificando a lista original): " + str(lugares))

lugares.sort(reverse=True)
print("Lista ordenada de forma reversa (modificando a lista original): " + str(lugares))
