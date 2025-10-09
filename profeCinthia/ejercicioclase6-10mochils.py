mochila = []

# Definir tamaño de la mochila
while True:
    try:
        capacidad = int(input("Ingrese de qué tamaño quiere la mochila (cant. de elementos): "))

        if capacidad <= 0:
            print("Debes ingresar un número positivo mayor que cero.")
            continue  

        print(f"Tu mochila será de {capacidad} elementos.")
        mochila = [0] * capacidad  
        break 

    except ValueError:
        print("Debes ingresar un valor numérico válido.")

print("\nContenido inicial de la mochila:", mochila)

# Menú principal
while True:
    print("\n=== MENÚ MOCHILA ===")
    print("1- AGREGAR OBJETO MÁGICO")
    print("2- VER MOCHILA")
    print("3- SALIR")

    try:
        opc = int(input("Ingrese la opción que quiera realizar: "))
        if opc < 1 or opc > 3:
            print("Debes ingresar una opción válida (1 a 3).")
            continue
    except ValueError:
        print("Debes ingresar un valor numérico válido.")
        continue

    if opc == 1:
        try:
            posicion = int(input(f"Ingrese la posición (1 a {capacidad}) donde quiere guardar un objeto: "))
            if posicion < 1 or posicion > capacidad:
                print("Posición fuera del rango de la mochila.")
                continue

            objeto = input("Ingrese el nombre del objeto mágico: ")
            mochila[posicion - 1] = objeto
            print(f"Objeto '{objeto}' guardado en la posición {posicion}.")
        except ValueError:
            print("Debes ingresar una posición numérica válida.")

    elif opc == 2:
        print("\nContenido actual de la mochila:")
        for i, item in enumerate(mochila, start=1):
            print(f"Posición {i}: {item}")

    elif opc == 3:
        print("Saliendo ...........................................................................................................")
        break



    




        
    

