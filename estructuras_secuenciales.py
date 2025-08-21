# Imprimir "Hola Mundo"
print("Hola Mundo!")


# Pedir nombre y saludar
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")


# Pedir datos personales y mostrarlos
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


# Área y perímetro de un círculo
radio = float(input("Ingrese el radio del círculo: "))
area = 3.14 * (radio ** 2)
perimetro = 2 * 3.14 * radio
print(f"El área es {area} y el perímetro es {perimetro}")


# Convertir segundos en horas
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas")


# Tabla de multiplicar
numero = int(input("Ingrese un número: "))

print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")



# Operaciones con dos números
a = int(input("Ingrese el primer número para operar: "))
b = int(input("Ingrese el segundo número: "))
print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
print(f"División: {a / b}")


# Índice de Masa Corporal (IMC)
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Su IMC es: {imc}")


# Celsius a Fahrenheit
celsius = float(input("Ingrese la temperatura en °C: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius} °C equivalen a {fahrenheit} °F")


# Promedio de tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio es: {promedio}")
