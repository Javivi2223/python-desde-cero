# La sintaxis para acceder a los elementos es con el nombre de la variable que tiene la listas seguida de los corchetes [] con su índice al interior

fruits = ["apple","orange","pineapple"]
print(fruits[0])

# Los elementos en una lista tienen una posición numérica partiendo desde el 0

# Las listas son modificables, es decir, pueden mutar. En otras palabras las listas con mutables, a diferencia de los strings que son inmutables.

fruits[0] = "chocolate"

print(fruits)

# Ejemplo, los strings son inmutables, es decir una vez que se establece su valor, este no se puede modificar

some_string = "Mundo"

print(some_string[0])