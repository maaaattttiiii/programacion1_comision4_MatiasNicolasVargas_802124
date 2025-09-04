#EJERCICIO FOR 

print("\n =========QUE MENSAJE QUIERE ENVIAR=========")
alfabeto = "abcdefghijklmnñopqrstuvwxyz"

corrimiento = int(input("Ingrese cuanto quiere que se corran las letras: "))

for i in range(5):
    mensaje = input(f"Ingrese el mensaje {i+1}: ")
    encriptado = ""

    for letra in mensaje:
        if letra.lower() in alfabeto:  
            indice = alfabeto.index(letra.lower())
            nuevo = (indice + corrimiento) % 27
            nueva = alfabeto[nuevo]
            if letra.isupper():
                encriptado += nueva.upper()
            else:
                encriptado += nueva
        else:
            encriptado += letra  

    print("Mensaje encriptado:", encriptado)


#EJERCICIO WHILE

import random

while True:
    print("\n==== QUE ELIGES ESTA RONDA ====")
    print("1. Piedra")
    print("2. Papel ")
    print("3. Tijera")
    print("4. No quiero jugar tengo miedo")

    opcion = int(input("te espero...: "))

    if opcion == 1:
        opcion1 = random.randint(1,3)
        if opcion1 == 2 :
            print("looser")
        elif opcion1 == opcion:
            print("crack, pareciera que sos vos la maquina, sacamos lo mismo ")
        else : 
            print("aaa no, pero vos sos una bestia")
            
    elif opcion == 2:
        opcion1 = random.randint(1,3)
        if opcion1 == 3 :
            print("looser")
        elif opcion1 == opcion: 
            print("crack, pareciera que sos vos la maquina, sacamos lo mismo ")
        else: 
            print("pero estamos hablando de un prodigio me parece, que capo")
            
    elif opcion == 3:
        opcion1 = random.randint(1,3)
        if opcion1 == 1 :
            print("looser")
        elif opcion1 == opcion: 
            print("crack, pareciera que sos vos la maquina, sacamos lo mismo ")
        else: 
            print("che... me sorprenden tus habilidades en este jueguito")
        
        
        
    elif opcion == 34:
        print("Saliendo entonces...")
        break

    else:
        print("❌ Opción no válida")



