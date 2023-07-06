size = int(input("dime un numero: "))
for y in range(size):
  line = ""
  for x in range(size):
    if (x == y) or (x == size):
      line += "*"
    else:
      line += " "
  print(line)