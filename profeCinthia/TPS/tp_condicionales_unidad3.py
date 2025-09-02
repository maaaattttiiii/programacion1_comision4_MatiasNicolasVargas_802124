#1: mayor de edad
print("\n -------------------------------------------------------------")

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")

#2: notas 
print("\n -------------------------------------------------------------")

nota = float(input("Ingrese su nota: "))
if nota >= 6: 
    print("Aprobado")
else: 
    print("Desaprobado")

#3: número pares
print("\n -------------------------------------------------------------")

num = float(input("Ingrese un número: "))
if num%2 == 0 :
    print("Ha ingresado un número par")
else: 
    print("Por favor, ingrese un número par")

#4: categoria de edad
print("\n -------------------------------------------------------------")

edad = int(input("Ingrese su edad: "))
if edad < 12: 
    print("Estás en la categoría Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#5: contraseñas
print("\n -------------------------------------------------------------")

contraseña = input("Ingrese una contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6: moda, mediana y media
print("\n -------------------------------------------------------------")

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Lista:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No cumple estrictamente ninguna condición de sesgo")

#7: str con ! al final 
print("\n -------------------------------------------------------------")

frase = input("Ingrese una frase o palabra: ")

if frase[-1].lower().strip() in "aeiou":
    frase += "!"
print(frase)

#8: nombre en distintas formas
print("\n -------------------------------------------------------------")

nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese 1 (mayúsculas), 2 (minúsculas) o 3 (primera letra mayúscula): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida")

#9: terremotos
print("\n -------------------------------------------------------------")

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#10: estaciones del año
print("\n -------------------------------------------------------------")

hemisferio = input("Ingrese su hemisferio (Norte/Sur): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

if (mes == 12 and dia >= 21) or (1 == mes <= 2) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
else:  
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"

if hemisferio == "NORTE":
    print("Estación:", estacion_norte)
elif hemisferio == "SUR":
    print("Estación:", estacion_sur)
else:
    print("Hemisferio no válido")

