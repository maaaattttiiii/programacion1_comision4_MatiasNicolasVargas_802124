excursiones = []
cupos = []

while True:
    print("\nMENÚ PRINCIPAL")
    print("\n1- AGREGAR EXCURSIONES")
    print("2- AGREGAR CUPOS POR EXCURSIÓN")
    print("3- MOSTRAR EXCURSIONES CON SUS CUPOS")
    print("4- CONSULTAR CUPOS POR NOMBRE")
    print("5- EXCURSIONES SIN CUPOS")
    print("6- AGREGAR EXCURSIONES INDIVIDUAL")
    print("7- ACTUALIZAR CUPOS POR EXCURSIÓN")
    print("8- SALIR")

    opc = input("Ingrese la opción que quiera realizar: ")

    if not opc.isdigit(): 
        print("ERROR! debe ingresar valor numérico positivo (1 al 8)")
        continue
    opc = int(opc)
    
    if opc>8 or opc<1:
        print("ERROR! el índice tiene que estar entre el 1 y el 8")
        continue
    
    if opc == 1:
        print("\n1- AGREGAR EXCURSIONES")
        num_exc = input("Cuántas excursiones quiere agregar?: ")
    
        if num_exc.isdigit():
            num_exc = int(num_exc)
        else:
            print("ERROR! debe ingresar valores numéricos positivos")
        
        for i in range(num_exc):
            excursion = input(f"Ingrese el nombre de la excursión {i+1}: ").strip().lower()
            if excursion in excursiones:
                print("ERROR! La opción que desea ingresar ya está registrada")
            elif excursion == "":
                print("ERROR! No se puede dejar el espacio vacío")
            else:
                excursiones.append(excursion)
                cupos.append(0)
    if opc == 2:
        print("\n2- AGREGAR CUPOS POR EXCURSIÓN")
        if len(excursiones) == 0:
            print("ERROR! no hay excursiones cargadas todavia, vuelva a la opción 1")
        for i in range(len(excursiones)):
            cupo = input(f"Ingrese la cantidad de cupos para la excursion {excursiones[i]}: ")
            if cupo.isdigit():
                cupo = int(cupo)
                cupos[i]= cupo
                print(f"\n Ahora la excursión {excursiones[i]}, tiene {cupos[i]} cupo/s")
            else:
                print("ERROR! debe ingresar valores numéricos positivos")
    if opc == 3:
        print("\n3- MOSTRAR EXCURSIONES CON SUS CUPOS")
        if len(excursiones) == 0:
            print("ERROR! no hay excursiones cargadas todavia, vuelva a la opción 1")
        for i in range(len(excursiones)):
            print(f"\n La excursión {excursiones[i]}, tiene {cupos[i]} cupo/s")
    if opc == 4 :
        print("\n4- CONSULTAR CUPOS POR NOMBRE")
        if len(excursiones) == 0:
            print("ERROR! no hay excursiones cargadas todavia, vuelva a la opción 1")
        consulta = input("Ingrese el nombre de la excursión de la que quiere consultar: ").strip().lower()
        if consulta in excursiones:
            idx = excursiones.index(consulta)
            print(f"\n La excursión {excursiones[idx]}, tiene {cupos[idx]} cupos")
        else:
            print("La excursión por la que consulta no existe o está mal escrita")
    if opc == 5:
        print("\n5- EXCURSIONES SIN CUPOS")
        if len(excursiones) == 0:
            print("ERROR! no hay excursiones cargadas todavia, vuelva a la opción 1")
        for i in range(len(excursiones)):
            if cupos[i] == 0:
                print(f"- {excursiones[i]}, tiene 0 cupos")
    if opc == 6 :
        print("\n6- AGREGAR EXCURSIONES")
        nueva_exc = input("Ingrese el nombre de la excursión que quiere agregar: ").strip().lower()
        if nueva_exc in excursiones:
            print("ERROR! La opción que intenta agregar ya está cargada")
        elif nueva_exc == "":
            print("ERROR! No se puede dejar vacía esta opción") 
        else:
            print("Nueva excursión cargada con éxito")
            excursiones.append(nueva_exc)
        cupo_nueva = input("Ingrese cuántos cupos tiene esta nueva excursión: ")
        if cupo_nueva.isdigit():
            cupo_nueva = int(cupo_nueva)
            cupos.append(cupo_nueva)
            print(f"\n Ahora la nueva excursión {nueva_exc}, tiene {cupo_nueva} cupo/s")
        else:
            print("ERROR! debe ingresar valores numéricos positivos")
    if opc == 7:
        print("\n7- ACTUALIZAR CUPOS POR EXCURSIÓN")
        if len(excursiones) == 0:
            print("ERROR! no hay excursiones cargadas todavia, vuelva a la opción 1")
        excursion1 = input("Ingrese el nombre de la excursión a la que le quiere actulizar los cupos: ").strip().lower()
        if not excursion1 in excursiones:
            print("ERROR! La excursión que ingresó no existe o está escrita")
        elif excursion1 == "":
            print("ERROR! No se puede dejar vacío este espacio")
        else:
            idx = excursiones.index(excursion1)
        
        actualizacion = input("Ingrese el valor actualizados de cupos: ")
        if actualizacion.isdigit():
            actualizacion = int(actualizacion)
            cupos[idx] = actualizacion
            print(f"\n Ahora la excursión {excursiones[idx]}, tiene {cupos[idx]} cupo/s")
        else:
            print("ERROR! debe ingresar valores numéricos positivos")
    if opc == 8:
        break





        
    

            
