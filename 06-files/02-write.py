# para escribir utilizamos el modo w conm la funcion open

data = open('sample_two.txt', 'w')

for i in range(4):
  data.write(f"Chao pescao {i} \n")

data.close()      