print("\n ===ESPECIALIDADES Y SUS TURNOS===")

especialidades = []
turnos = []

while True:
    print("--------------------------------------------------------------")
    print("1- INGRESAR LISTA DE ESPECIALIDADES")
    print("2- INGRESAR LISTA DE TURNOS DISPONIBLES POR ESPECIALIDAD")
    print("3- MOSTRAR AGENDA")
    print("4- CONSULTAR CUPOS DE UNA ESPECIALIDAD")
    print("5- LISTA DE ESPECIALIDADES SIN CUPO")
    print("6- AGREGAR NUEVA ESPECIALIDAD")
    print("7- ACTUALIZAR CUPOS")
    print("8- AGENDA PARA PACIENTES(Con horarios)")
    print("9- SALIR")
    print("\n--------------------------------------------------------------")

    op= int(input("Ingrese la opcion que quiera realizar..."))
    print()
    print("INGRESAR LISTA DE ESPECIALIDADES")

    if op == 1:
        n1= int(input("Ingrese la cantidad de especialidades que quiere agregar: "))
        while True:
            if n1 > 0:
                break
            else:
                print("ERROR! No se permite ingresar números negativos o cero")
                n1= int(input("Ingrese la cantidad de especialidades que quiere agregar: "))


        for i in range(n1):
            esp = input(f"Ingrese la especialidad {i+1}: ")
            especialidades.append(esp)
        print(especialidades)
