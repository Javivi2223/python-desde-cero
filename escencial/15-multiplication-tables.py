#ejercicio. utilizando for y range, crear un algoritmo que imprima en la terminal las tablas de multiplicar desde el 1 al 12

for table in range(1,13):
    print(f"la tabla del {table}")
    for step in range(1,13):
       print(f"{table} x {step} = {table*step}")
       
 


