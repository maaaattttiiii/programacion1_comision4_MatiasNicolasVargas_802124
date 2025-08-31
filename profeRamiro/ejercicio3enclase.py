#EJERCICIO 3: 

def validar_cuil(cuil: str) -> bool:
    partes = cuil.split("-")
    if len(partes) != 3: 
        return False  
    if not (partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit()):
        return False 
    if partes[0] not in ("20", "23", "24", "27"): 
        return False
    if len(partes[1]) != 8: 
        return False 
    if len(partes[2]) != 1: 
        return False 
    return True


def monto_maximo(ingresos: float, años_trabajo: int, historial: int) -> float:
    
    if historial == 3:  
        return 0
    if ingresos < 200000:
        return 0
    if ingresos >= 200000 and años_trabajo < 2:
        return 500000
    if ingresos >= 200000 and años_trabajo >= 2:
        if historial == 2:  
            return 1000000
        elif historial == 1:  
            return 3000000
    return 0



nombre = input("Ingrese su nombre y apellido: ")
cuil = input("Ingrese cuil formato xx-12345678-x: ")

while not validar_cuil(cuil):
    print("CUIT inválido. Intente nuevamente.")
    cuil = input("Ingrese cuil formato xx-12345678-x: ")

monto = float(input("Ingrese el monto del crédito que quiere: "))
historial = int(input("Ingrese su historial (bueno: 1 , regular: 2 , malo: 3): "))
años_trabajo = int(input("Ingrese la cantidad de años que lleva trabajando: "))
ingresos = float(input("Ingrese el monto que cobra por mes (sin puntos ni coma): $ "))

monto_aprobado = monto_maximo(ingresos, años_trabajo, historial)

if monto_aprobado > 0 and monto <= monto_aprobado:
    print("✔ Su crédito fue aprobado\n")
    print("Cliente:            ",nombre)
    print("Cuil:               ",cuil)
    print(f"Ingresos:            ${ingresos}")
    print("Antigüedad:         ",años_trabajo, "años")
    print("Historial:          ",historial, "(bueno=1, regular=2, malo=3)")
    print(f"Monto aprobado:      ${monto}")
else:
    print("❌ Su crédito fue rechazado")
    if monto_aprobado > 0:
        print(f"👉 El máximo que podría solicitar es: ${monto_aprobado}")




