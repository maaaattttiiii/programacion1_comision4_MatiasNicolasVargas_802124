print("\n=====BIENVENIDO AL BINGO=====")
import random 
from random import choice 
filas = 5
columnas = 5
carton =[[0 for _ in range(5)]for _ in range(5)]
numeros = random.sample(range(1,51), 25)
for i in range(filas):
    for j in range(columnas):
        carton[i][j]= random.choice(numeros)

print("\nTU CARTÓN ES EL SIGUIENTE.....") 

for i in range(5):
    for j in range(5):
        print(carton[i][j], end = " ")
    print(" ")

win = False
 
while win == False:
    for i in range(5):
        for j in range(5):
            sorteo = random.randint(1,51)
            print("SALIÓ EL NÚMERO: ",sorteo)
            if sorteo in carton:
                print(f"Lo tienes")
                carton[i][j]= 0
            else:
                print("No lo tienes")
            