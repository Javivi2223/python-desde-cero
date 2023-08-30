english_to_spanish = {"one":"uno","two":"dos"}

#al igual que con .values(), tenemos el .keys(), que retorna un l,istado de las llaves

keys = english_to_spanish.keys() # => ["one, "two"]

for key in keys:
  print(f"{key} => {english_to_spanish[key]}")    