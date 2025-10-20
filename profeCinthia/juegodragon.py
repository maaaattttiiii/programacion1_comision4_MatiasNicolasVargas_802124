# Laberinto de ejemplo
# "X" = pared
# " " = camino
# "S" = salida
# "D" = dragón (inicio)

laberinto = [
    ["🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱"],
    ["🧱", "🐱‍🏍", " ", " ", " ", " ", "🧱"],
    ["🧱", "🧱", "🧱", " ", "🧱", " ", "🧱"],
    ["🧱", " ", " ", " ", "🧱", " ", "🎁"],
    ["🧱", " ", "🧱", "🧱", "🧱", "🧱", "🧱"]
]

# Buscar posición inicial del dragón
for i in range(len(laberinto)):
    for j in range(len(laberinto[i])):
        if laberinto[i][j] == "🐱‍🏍":
            fila, columna = i, j

pasos = 0

def mostrar_laberinto():
    for fila_l in laberinto:
        print("".join(fila_l))
    print()

while True:
    mostrar_laberinto()
    movimiento = input("Mover (w=arriba, s=abajo, a=izquierda, d=derecha, q=salir): ").lower()

    if movimiento == "q":
        print("El dragón se rindió 😔")
        break

    # Coordenadas nuevas según el movimiento
    nueva_fila, nueva_col = fila, columna

    if movimiento == "w":
        nueva_fila -= 1
    elif movimiento == "s":
        nueva_fila += 1
    elif movimiento == "a":
        nueva_col -= 1
    elif movimiento == "d":
        nueva_col += 1
    else:
        print("Movimiento inválido.")
        continue

    # Comprobamos límites
    if nueva_fila < 0 or nueva_fila >= len(laberinto) or nueva_col < 0 or nueva_col >= len(laberinto[0]):
        print("¡No podés salirte del laberinto! 🚫")
        continue

    # Obtenemos el contenido de la celda destino
    destino = laberinto[nueva_fila][nueva_col]

    if destino == "🧱":
        print("¡Te chocaste con una pared! 🧱")
        continue
    elif destino == "🎁":
        pasos += 1
        print(f"\n🐉 ¡El dragón encontró la salida en {pasos} pasos! ✨")
        break
    elif destino == " ":
        # Mover al dragón
        laberinto[fila][columna] = "."
        fila, columna = nueva_fila, nueva_col
        laberinto[fila][columna] = "🐱‍🏍"
        pasos += 1
    else:
        print("Movimiento no permitido.")

print("\nCamino recorrido final:")
mostrar_laberinto()
