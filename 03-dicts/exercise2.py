lenguaje = input("¿qué tipo de lenguaje quieres conocer?: ")

lenguajes = {}

lenguajes["python"] = "lenguaje moderno utilizado para todo tipo de aplicaciones"
lenguajes["ruby"] = "lenguaje completamente orientado a objetos"
lenguajes["javascript"] = "lenguaje para la web y servidores"

if lenguaje in lenguajes:
  print(f"si está {lenguaje}")
  print(f"su valor es: {lenguajes[lenguaje]}") 
else:
  print(f"no conozco el lenguaje {lenguaje}")  