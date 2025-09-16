print("\n ===BIBLIOTECA ONLINE===")

libros = []
ejemplares = []

while True: 
    
    print("1- AGREGAR LIBROS POR NOMBRE")
    print("2- AGREGAR EJEMPLARES DE LIBRO POR NOMBRE")
    print("3- CONSULTAR STOCK")
    print("4- CONSULTAR STOCK POR LIBRO")
    print("5- VER LIBROS QUE TIENEN 0 EJEMPLARES ")
    print("6- AGREGAR NUEVO LIBRO A LA LISTA")
    print("7- ACTUALIZAR EJEMPLARES")
    print("8- VER CATÁLOGO LIBROS DISPONIBLES")
    print("9- SALIR")
    opcion = int(input("Ingrese la opcion que quiera realizar: "))
    if opcion == 1:
        cantidad = int(input("Okey, Cuántos libros quiere agregar?..."))
        for i in range(cantidad) :
            libro = input(f"Ingrese el nombre del libro {i+1}: ")
            libros.append(libro)
    if opcion == 2:
        for i  in range(len(libros)):
            copias = int(input(f"Ingrese la cantidad de ejemplares de ({libros[i]}): "))
            ejemplares.append(copias)
    if opcion == 3:
        print("A continuación se le mostrará el stock de todos lo libros...")
        for i in range(len(libros)):
            print(f" El libro ({libros[i]}), tiene {ejemplares[i]} ejemplar/es")
    if opcion == 4:
        for i in range(len(libros)):
            print(f"{i} - {libros[i-1]}")
        indice = int(input("De qué libro quiere saber el stock(ingrese el índice del libro): "))
        print(f"El libro {libros[indice]}, tiene {ejemplares[i]} ejemplar/es")
    if opcion == 5:
        for i in range(0 , len(libros)):
            if ejemplares[i] == 0:
                print(f"---> {libros[i]}")
    if opcion == 6:
        nuevo_libro = input(print("Cuál es el título del nuevo libro que quiere agregar?: "))
        ejemplares_nuevo = int(input("Cuántos ejemplares de este nuevo libro hay?: "))
        libros.append(nuevo_libro)
        ejemplares.append(ejemplares_nuevo)
        

