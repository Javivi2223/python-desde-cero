#tarea: utilizando for e if dibujar un cuadrado en la terminal
for y in range(1,12):
  line = ""  
  for x in range(1,12):
    if (x == y) or (x + y == 12):
      line += "*"
    else:
      line += " "      
  print(line)     