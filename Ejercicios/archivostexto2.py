"""
archivo = open("datos.txt" , "w")
archivo.write("Saludo para todos")
archivo.close() 
"""
# Otra forma de escribir un archivo es utilizando with, 
# que se encarga de cerrar el archivo automáticamente
with open("datos2.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Saludo para todos")
    
# Leer un archivo utilizando with
with open("datos2.txt", "r", encoding="utf-8") as archivo:
    linea = archivo.readline()
    print(linea)
    
# Agregar texto a un archivo utilizando with
with open("datos2.txt", "a", encoding="utf-8") as archivo:
    archivo.write("\nQue onda pues peladitos?")
    
with open("datos2.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    print(lineas)
# Otra forma de leer un archivo es utilizando un bucle for, que itera sobre cada línea del archivo    
    for x in lineas:
        x = x.rstrip('\n')
        print(x)