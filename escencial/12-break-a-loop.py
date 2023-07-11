#patra salir del loop bajo cierta condicion podemos utilizar la estructura de control if junto con la palabra clave break

for letter in "murcielago":
  if letter == "a":
    break
  print(letter)

print("esto es después del loop")