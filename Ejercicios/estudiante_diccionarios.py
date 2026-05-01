#Ejercicio: Sistema de Gestión de Estudiantes
#Crea un programa que gestione las calificaciones de estudiantes usando diccionarios. El programa debe permitir:

estudiantes = {}
opcion = 0

menu ="""
*******Sistema de Gestión de Estudiantes*******

1. Agregar un nuevo estudiante
2. Agregar calificaciones a un nuevo estudiante
3. Calcular el promedio de  un estudiante
4.Mostrar todos los estudiantes con susu promedios 
5. Encontrar al estudiante con el promedio mas alto
6. Eliminar un estudiante
7. Salir
"""
while opcion != 7:
    print(menu)
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre in estudiantes:
            print("El estudiante ya existe")
        else:
            estudiantes[nombre] = {}
            print(f"Estuadiante {nombre} agregado exitosamente. ")
            print(estudiantes)
    elif opcion == 2:
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre in estudiantes:
            calificacion = float(input("Ingrese la  calificacion  : "))
            estudiantes[nombre].append(calificacion)
            print(f"calificacion {calificacion} agegada a {nombre}.")
        else : 
            print("El estudiante no existe: ")
        print("estudiantes")
    elif opcion == 3:
        nombre = input ("Ingrese el nombre del esttudiate: " )
        if nombre in estudiantes:
            if len(estudiantes[nombre]) > 0:
                promedio = sum(estudiantes[nombre]) / len(estudiantes[nombre])
                print(f"El promedio de {nombre} es : {promedio:2f}")

            

