habitaciones = []
estado = []

while True:
    print("===MENÚ DE HABITACIONES===")
    print("1- CARGAR HABITACIONES")
    print("2- CARGAR ESTADO DE LA HABITACIÓN")
    print("3- LISTA DE ESTADO GENERAL")
    print("4- CONSULTA DE ESTADO INDIVIDUAL")
    print("5- LISTAR OCUPADAS O LIBRES")
    print("6-")
    print("7-")
    print("8-")
    print("9-")

    opc = input("Ingrese la opción que quiera realizar: ")
    if not opc.isdigit():
        print("ERROR! Ingrese un valor positivo entre el 1 y el 8") 
        continue

    opc = int(opc)   

    if opc == 1:
        cant= input("Ingrese cuantas habitaciones quiere cargar: ").strip()
        if not cant.isdigit():
            print("ERROR! Ingrese un número positivo") 
            continue
        if cant == "":
            print("ERROR! El valor no puede estar vacío")
            continue
        cant = int(cant)
        for i in range(cant):
            habitacion = input("Ingrese el número de habitación que quiera cargar: ").strip()
            if not habitacion.isdigit():
                print("ERROR! Ingrese un número positivo") 
                continue
            elif habitacion == "":
                print("ERROR! El valor no puede estar vacío")
                continue
            habitacion = int(habitacion)
            if habitacion in habitaciones:
                print("ERROR! El valor que intenta ingresar ya fue cargado")
                continue
            else:
                habitaciones.append(habitacion)
                estado.append(0)
    elif opc == 2:
        if len(habitaciones) == 0:
            print("ERROR! Todavía no hay habitaciones cargadas, vuelva a la opción 1")
            continue
        for i in range(len(habitaciones)):
            estados = input(f"Ingrese el estado de la habitación {habitaciones[i]}(0: libre, 1: ocupada): ")
            if not estados.isdigit():
                print("ERROR! Ingrese 0 o 1 ") 
                continue
            elif estados == "":
                print("ERROR! El valor no puede estar vacío")
                continue
            estados = int(estados)
            if estados <0 or estados >1:
                print("ERROR! Ingrese 0 o 1 ") 
                continue
            estado[i] = estados
            if estado[i] == 1:
                print(f"La habitación {habitaciones[i]}, está ocupada ({estado[i]})")
            elif estado[i] == 0:
                print(f"La habitación {habitaciones[i]}, está libre ({estado[i]})")
    elif opc == 3:
        if len(habitaciones) == 0:
            print("ERROR! Todavía no hay habitaciones cargadas, vuelva a la opción 1")
            continue
        for i in range(len(habitaciones)):
            if estado[i] == 1:
                print(f"La habitación {habitaciones[i]}, está ocupada ({estado[i]})")
            elif estado[i] == 0:
                print(f"La habitación {habitaciones[i]}, está libre ({estado[i]})")
    elif opc == 4:
        if len(habitaciones) == 0:
            print("ERROR! Todavía no hay habitaciones cargadas, vuelva a la opción 1")
            continue
        consulta = input("Ingrese el número de la habitación por la que quiere consultar: ")
        if not consulta.isdigit():
            print("ERROR! Ingrese 0 o 1 ") 
            continue
        elif consulta == "":
            print("ERROR! El valor no puede estar vacío")
            continue
        consulta = int(consulta)
        if not consulta in habitaciones:
            print(f"La habitación {consulta} no se encuentra registrada")
        elif consulta in habitaciones: 
            idx = habitaciones.index(consulta)
            if estado[idx] == 1:
                print(f"La habitación {habitaciones[idx]}, está ocupada ({estado[idx]})")
            elif estado[idx] == 0:
                print(f"La habitación {habitaciones[idx]}, está libre ({estado[idx]})")
    elif opc == 5:
        if len(habitaciones) == 0:
            print("ERROR! Todavía no hay habitaciones cargadas, vuelva a la opción 1")
            continue
        lista = input("Desea una lista de las habitaciones libres(L) o ocupadas(O): ").upper().strip()
        if lista == "L":
            for i in range(len(habitaciones)):
                if estado[i] == 1:
                    print(f"- La habitación {habitaciones[i]} está libre")
        elif lista == "O":
            for i in range(len(habitaciones)):
                if estado[i] == 0:
                    print(f"- La habitación {habitaciones[i]} está ocupada")
        else:
            print("ERROR! La opción que ingresó es inválida")
    elif opc == 6:
        habitacion1 = input("Ingrese el número de habitación que quiera cargar: ").strip()
        if not habitacion1.isdigit():
            print("ERROR! Ingrese un número positivo") 
            continue
        elif habitacion1 == "":
            print("ERROR! El valor no puede estar vacío")
            continue
        habitacion1 = int(habitacion1)
        if habitacion1 in habitaciones:
            print("ERROR! El valor que intenta ingresar ya fue cargado")
            continue
        else:
            habitaciones.append(habitacion1)
        estados1 = input(f"Ingrese el estado de la habitación que acaba de ingresar(0: libre, 1: ocupada): ")
        if not estados1.isdigit():
            print("ERROR! Ingrese 0 o 1 ") 
            continue
        elif estados1 == "":
            print("ERROR! El valor no puede estar vacío")
            continue
        estados1 = int(estados1)
        if estados <0 or estados >1:
            print("ERROR! Ingrese 0 o 1 ") 
            continue
        estado.append(estados1)
        if estados1 == 1:
            print(f"La habitación nueva está ocupada")
        elif estado[i] == 0:
            print(f"La habitación nueva está libre")
    elif opc == 7:
        if len(habitaciones) == 0:
            print("ERROR! Todavía no hay habitaciones cargadas, vuelva a la opción 1")
            continue
        for i in range(len(habitaciones)):
            if estado[i] == 1:
                print(f"- La habitación {habitaciones[i]} está libre")
    elif opc == 8:
        
    elif opc == 9:
        break


    

        

        

            


            

            

        
        
