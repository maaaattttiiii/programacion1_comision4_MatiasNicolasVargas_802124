print("=====BIENVENIDO AL BINGO=====")
print("Ahora le damos su cartón...")

import random 
num = random.sample(range(1,51), 25)
carton = []
for i in range (0,25,5):
    fila = num[i:i+5]
    carton.append(fila)

for fila in carton:
    for num in fila:
        print(f"{num}" , end = " ")
    print()
print()

lista = list(range(1,51))
random.shuffle(lista)

while True: 
    salida = input("1- Pecione (S) si quiere salir del juego, si no cualquier letra para continuar").lower()
    input("2- Precione cualquier letra o símbolo para sacar un número...")

    if salida == "s":
        break
   
    sorteo = lista.pop()
    
    encontrado = False 
    for i in range(5):
        for j in range(5):
            if carton[i][j] == sorteo:
                encontrado = True 
                carton[i][j] = 0
    
    if encontrado == True: 
        print(f"Salió el número {sorteo} y si lo tienes")
    else: 
        print(f"Salió el número {sorteo}, no lo tienes")
    
    linea = False

    for fila in carton:
        if fila == [0,0,0,0,0]:
            linea = True
    
    if linea == True: 
        print("LINEAAA, tienes linea en tu tablero")
    
    bingo = True

    for filas in carton:
        for num in filas:
            if num != 0:
                bingo = False
     
    for fila in carton:
        for num in fila:
            print(f"{num}" , end = " ")
        print()
    print()

    if bingo:
        print("BIIIIIIIINNNNGOOOOOO, GANASTE FACHA SOS CRACK")
        break
    
    

    




