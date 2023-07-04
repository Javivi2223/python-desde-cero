#dibujar una x  de tamaño 12 utilizando el *
print("*               *")
print("  *           *")
print("    *       *")
print("      *   *")
print("        *")
print("      *  *")
print("    *       *")
print("  *           *")
print("*               *")

print("--------------------")

for y in range(1,11):
  line = ""  
  for x in range(1,11):
    if (x == y) or (x + y == 12):
      line += "*"
    else:
      line += " "      
  print(line)     