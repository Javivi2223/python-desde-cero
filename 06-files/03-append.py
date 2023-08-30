# con append podemos agregar más información al archivo

dataFile = open('./sample_two.txt', 'a')

for i in range(4):
  dataFile.write(f"A la {i} \n")

dataFile.close()    