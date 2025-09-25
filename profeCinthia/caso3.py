tarjetas= []
saldo = []

while True:
    print("------------------------------------------------")
    print("\nSISTEMA SUBE")
    print("--> MENÚ ")
    print("1- AGREGAR TARJETAS SUBE")
    print("2- AGREGAR SALDO DE LAS TARJETAS") 
    print("3- MOSTRAR TARJETAS Y SALDOS") 
    print("4- CONSULTAR SALDO POR NÚMERO") 
    print("5- LISTA DE SALDOS NEGATIVOS O CERO") 
    print("6- AGREGAR NUEVA TARJETA") 
    print("7- CARGAR/DEBITAR SALDOS") 
    print("8- VER TODAS LAS TARJETAS Y SUS SALDOS") 
    print("9- SALIR") 

    opc = int(input("\nIngrese la opción que vaya a realizar: "))
    
    if opc == 1:
        cant = input("Cuantas tarjetas quiere agregar? --->")
        if cant.isdigit: 
            int(cant)
            for i in range(cant):
                sube = input(f"Ingrese el número de la tarjeta {i+1}: ").strip()
                if sube in tarjetas:
                    print("ERROR! Esta tarjeta ya está cargada en el sitema")
                elif sube == "":
                    print("ERROR! No se puede dejar un espacio vacío")
                else:
                    tarjetas.append(sube)
        else:
            print("ERROR! Debe poner un número de tarjetas a agregar")
    elif opc == 2:
        if range(tarjetas) == 0:
            print("ERROR! Todavía no se cargan tarjetas en el sitema, vuelva a la opción 1 y registre las tarjetas")
        for i in range(tarjetas):
            carga = input(f"Ingrese la cantidad que le quiera cargar a la tarjeta {i+1}: ")
            if carga.isdigit:
                int(carga)
    
        