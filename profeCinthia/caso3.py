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
        cant = int(input("Cuantas tarjetas quiere agregar? --->"))
        for i in range(cant):
            sube = input(f"Ingrese la tarjeta número {i+1}(solo números, 5 dígitos): ")
            if sube.isdigit and range(sube.strip) == 5:
                tarjetas.append(sube)
            else: 
                print("ERROR! , respete el formato indicado")