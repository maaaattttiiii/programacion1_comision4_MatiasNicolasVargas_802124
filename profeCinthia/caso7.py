alumnos = []
asistencia = []

while True:
    print("\n ---SISTEMA DE ASISTENCIA---")
    print("---> MENÚ")
    print("1- INGRESAR ALUMNOS")
    print("2- INGRESAR ASISTENCIA")
    print("3- MOSTRAR LISTA CON TODOS LOS ALUMNOS")
    print("4- CONSULTAR ASISTENCIA POR ESTUDIANTE")
    print("5- LISTAR AUSENTES")
    print("6- MARCAR ASISTENCIA POR ALUMNO")
    print("7- AGREGAR NUEVO ALUMNO")
    print("8- SALIR")
    print()

    opc= int(input("Ingrese la opción que vaya a realizar---> "))

    if opc>9 or opc<1:
        print("ERROR! opción inválida")
    elif opc == 1:
        cant= input("Ingrese cuantos alumnos quiere cargar: ")
        if cant.isdigit():
            cant = int(cant)
            for i in range(cant):
                alumno = input(f"Ingrese el alumno {i+1}: ").strip()
                if alumno == "":
                    print("ERROR! No se puede dejar vacío")
                elif alumno in alumnos:
                    print("ERROR! El alumno que intenta cargar ya está registrado")
                else:
                    alumnos.append(alumno)
                    asistencia.append(0)
        else:
            print("ERROR! Ingrese un valor válido")
    elif opc == 2:
        if len(alumnos) == 0:
            print("ERROR! Todavía no hay alumnos cargados vuelva a la opción 1")
        else:
            for i in range(len(alumnos)):
                asist = input(f"Ingrese la asitencia del alumno ({alumnos[i]}): ")
                if asist.isdigit():
                    asist = int(asist)
                    if asist <= 0:
                        print("ERROR! No se puede agregar asistencia negativa o 0")
                    else:
                        asistencia[i] = asist
    elif opc == 3:
        if len(alumnos) == 0:
            print("ERROR! Todavía no hay alumnos cargados vuelva a la opción 1")
        for i in range(len(alumnos)):
            print(f"{i+1}- El alumno {alumnos[i]}, tiene {asistencia[i]} en asistencia")
    elif opc == 4:
        if len(alumnos) == 0:
            print("ERROR! Todavía no hay alumnos cargados vuelva a la opción 1")
        name = input("Ingrese el nombre del estudiante que nesesite: ").strip()
        if name in alumnos:
            idx = alumnos.index(name)
            print(f"El alumno {alumnos[idx]}, tiene {asistencia[idx]} asistencias")
    elif opc == 5: 
        if len(alumnos) == 0:
            print("ERROR! Todavía no hay alumnos cargados vuelva a la opción 1")
        for i in range(len(asistencia)):
            if asistencia[i] == 0:
                print(f" El alumno {alumnos[i]}, tiene 0 asistencias")
    elif opc == 6:
        if len(alumnos) == 0:
            print("ERROR! Todavía no hay alumnos cargados vuelva a la opción 1")
        buscar = input("Ingrese el alumno para marcar asistencia: ").strip()
        if buscar in alumnos:
            i = alumnos.index(buscar)
            accion = input("¿si quiere sumar una asistencia aprete (S)").upper().strip()
            if accion == "S":
                asistencia[i] += 1
                print(f"{buscar} ahora tiene {asistencia[i]} asistencias")
            else:
                print("Opción inválida.")
        else:
            print("El alumno no existe")
    elif opc == 7:
        if len(alumnos) == 0:
            print("ERROR! Todavía no hay una lista de alumnos a la que se le puedan agregar nuevos, vuelva a la opción 1")
        nuevo = input("Ingrese el nombre del alumno que quiera agregar:").strip()
        if nuevo in alumnos:
            print("ERROR! El alumno ya se encuentra registrado")
        elif nuevo == "":
            print("ERROR! No se puede dejar el espacio vacío")
        else:
            alumnos.append(nuevo)
            asistencia.append(0)
    elif opc == 8:
        print("SALIENDO...")
        break


    





    








