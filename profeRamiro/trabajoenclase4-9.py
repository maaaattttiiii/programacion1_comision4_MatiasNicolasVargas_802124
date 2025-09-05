#patentes arg

patente = input("ingrese su patente sin espacios (formato AAA111): ").strip()
while not (patente[:3].isalpha() and patente[3:].isdigit() and len(patente) == 6):
    print("Formato de la patente ingresada inválido")
    patente = input("ingrese su patente sin espacios (formato AAA111): ").strip()


letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

corrimiento = int(input("Ingrese cuanto le quiere sumar a la patente: "))
encontrada = False
contador = 0


for a in letras:
    for b in letras:
        for c in letras:
            for n1 in range(10):
                for n2 in range(10):
                    for n3 in range(10):
                        actual = f"{a}{b}{c}{n1}{n2}{n3}"
                        if actual == patente:
                            encontrada = True
                        if encontrada:
                            if contador == corrimiento:
                                print("La nueva patente es:", actual)
                                exit()
                            contador += 1