#en python algunos tipos de valores son consideradas colecciones como las listas, diccionarios, strings, tuplas y sets. estas colecciones se pueden recorrer.
#con el for loop podemos ejecutar un conjunto de sentencias una por cada elemento de la coleccion

word = 'banana'
index = 0
while index < (len(word)):
  print(word[index])
  index += 1

print("-------------------")


for letter in 'banana':
  print(letter)