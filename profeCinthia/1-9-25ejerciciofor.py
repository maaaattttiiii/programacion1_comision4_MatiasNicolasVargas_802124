print("\n =========QUE MENSAJE QUIERE ENVIAR=========")
alfabeto = "abcdefghijklmnñopqrstuvwxyz"

corrimiento = int(input("Ingrese el corrimiento: "))

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

