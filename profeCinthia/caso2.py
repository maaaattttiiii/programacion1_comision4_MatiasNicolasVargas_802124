

especialidades = []
cupos = []

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Ingresar lista de especialidades")
    print("2. Ingresar lista de cupos disponibles por especialidad")
    print("3. Mostrar agenda")
    print("4. Consultar cupos de una especialidad")
    print("5. Listar especialidades sin cupo")
    print("6. Agregar especialidad")
    print("7. Ver sin cupo")
    print("8. Actualizar cupos (reservar/cancelar)")
    print("9. Ver agenda completa")
    print("10. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cant = input("¿Cuántas especialidades desea ingresar?: ")
        if cant.isdigit():
            cant = int(cant)
            for i in range(cant):
                nombre = input(f"Ingrese el nombre de la especialidad {i+1}: ").strip()
                if nombre == "":
                    print("⚠️ El nombre no puede estar vacío.")
                elif nombre in especialidades:
                    print("⚠️ La especialidad ya existe.")
                else:
                    especialidades.append(nombre)
                    cupos.append(0)  # Inicializamos cupo en 0 hasta que se carguen
        else:
            print("⚠️ Debe ingresar un número válido.")

    elif opcion == "2":
        if len(especialidades) == 0:
            print("⚠️ Primero debe ingresar especialidades (opción 1).")
        else:
            for i in range(len(especialidades)):
                while True:
                    cupo = input(f"Ingrese cupos disponibles para {especialidades[i]}: ")
                    if cupo.isdigit() and int(cupo) >= 0:
                        cupos[i] = int(cupo)
                        break
                    else:
                        print("⚠️ Ingrese un número válido (≥ 0).")

    elif opcion == "3":
        print("\n=== Agenda ===")
        for i in range(len(especialidades)):
            print(f"{especialidades[i]}: {cupos[i]} cupos")

    elif opcion == "4":
        buscar = input("Ingrese el nombre de la especialidad a consultar: ").strip()
        if buscar in especialidades:
            i = especialidades.index(buscar)
            print(f"{buscar}: {cupos[i]} cupos disponibles")
        else:
            print("⚠️ La especialidad no existe.")

    elif opcion == "5" or opcion == "7":  # Ambas opciones hacen lo mismo
        print("\n=== Especialidades sin cupo ===")
        sin_cupo = False
        for i in range(len(especialidades)):
            if cupos[i] == 0:
                print(f"{especialidades[i]}: Sin cupos")
                sin_cupo = True
        if not sin_cupo:
            print("Todas las especialidades tienen cupos disponibles.")

    elif opcion == "6":
        nombre = input("Ingrese el nombre de la nueva especialidad: ").strip()
        if nombre == "":
            print("⚠️ El nombre no puede estar vacío.")
        elif nombre in especialidades:
            print("⚠️ La especialidad ya existe.")
        else:
            while True:
                cupo = input(f"Ingrese cupos iniciales para {nombre}: ")
                if cupo.isdigit() and int(cupo) >= 0:
                    especialidades.append(nombre)
                    cupos.append(int(cupo))
                    print(f"✅ Especialidad {nombre} agregada con {cupo} cupos.")
                    break
                else:
                    print("⚠️ Ingrese un número válido (≥ 0).")

    elif opcion == "8":
        buscar = input("Ingrese la especialidad a actualizar: ").strip()
        if buscar in especialidades:
            i = especialidades.index(buscar)
            accion = input("¿Desea reservar (R) o cancelar (C) un turno?: ").upper()
            if accion == "R":
                if cupos[i] > 0:
                    cupos[i] -= 1
                    print(f"✅ Reserva realizada. {buscar} ahora tiene {cupos[i]} cupos.")
                else:
                    print("⚠️ No hay cupos disponibles para reservar.")
            elif accion == "C":
                cupos[i] += 1
                print(f"✅ Cancelación realizada. {buscar} ahora tiene {cupos[i]} cupos.")
            else:
                print("⚠️ Opción inválida.")
        else:
            print("⚠️ La especialidad no existe.")

    elif opcion == "9":
        print("\n=== Agenda completa ===")
        for i in range(len(especialidades)):
            print(f"{i+1}. {especialidades[i]} - Cupos: {cupos[i]}")

    elif opcion == "10":
        print("👋 Saliendo del sistema. ¡Gracias!")
        break

    else:
        print("⚠️ Opción inválida. Intente nuevamente.")
