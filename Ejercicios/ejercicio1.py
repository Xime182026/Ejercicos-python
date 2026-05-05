veterinaria = {}
while True:
    print("\n---Sistema de Veterinaria---")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del cliente: ")
        telefono = input("Ingrese el telefono del cliente:  ")
        veterinaria[nombre] = {"telefono": telefono, "mascota": {}}
        print(f"cliente{nombre} agregado exitosamente.")
        
    elif opcion == "2":
        cliente = input("Nombre del cliente: ")
        if cliente in veterinaria:
            mascota = input("Nombre de l a mascota: ")
            especie = input("Especie de la mascota: ")
            edad = int(input("Edad de la mascota: "))
            peso = float(input("peso de la mascota: "))
            veterinaria[cliente]["mascota"][mascota]={
                "especie" : especie,
                "edad" : edad,
                "peso" : peso,
                
            }
            print(f"mascota{mascota} agregada a cliente {cliente} exitosamente.")
        else:
            print("cliente no encontrado.")

    print("2. Agregar mascota")
    print("3. Mostrar datos de un cliente")
    print("4. Buscar mascota por nombre")
    print("5. Promedio peso de las mascotas")
    print("6. Mascota más pesada")
    print("7. Eliminar mascota")
    print("8. Eliminar Cliente")
    print("9. Salir")
    
        
