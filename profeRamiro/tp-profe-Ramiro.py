#EJERCICIO 6: CALIFICACION FINAL 

  #pedimos las tres notas de los parciales 

p1= float(input("Ingrese la nota del parcial uno: "))* 0.55
p2= float(input("Ingrese la nota del parcial dos: ")) * 0.55
p3= float(input("Ingrese la nota del parcial tres: ")) * 0.55

  #calculamos promedio de las tres notas 

promedio = (p1 + p2 + p3) / 3 

  #pedimos la nota del examen final

ex_final = float(input("Ingrese la nota del examen final: ")) * 0.3

  #pedimos la nota del integrador 

tp_final = float(input("Ingrese la nota del trabajo final: ")) * 0.15

  #mostramos nota final 

nota = promedio + ex_final + tp_final
print("La calificacion final de la materia fue de: ",nota)

print("-------------------------------------------------------------------")

#EJERCICIO 7: CONVERSIÓN DE DIVISAS

print("BUENAS, Ingrese un valor en dólares y se lo convertimos a (pesos arg, pesos col , o euros)")
print(                        "CAMBIOS")
print("1 dolar = 1300 ars") 
print("1 dolar = 4000 col" )
print("1 dolar = 0.86 eu")
dolar = float(input("Ingrese el valor aquí: "))
ars = dolar * 1300
col = dolar * 4000
eu = dolar * 0.86

print(f"La suma de, ${dolar} dolares , equivale a... ({ars} pesos argentinos ), ({col} pesos colombianos), ({eu} euros)")

print("-------------------------------------------------------------------")

#EJERCICIO 8: CÁLCULOS DE VIAJE

distancia =float(input("Ingrese la distancia del viaje en km: "))
precio = float(input("Ingrese el precio de la nafta por litro: "))
total_litros = distancia / 12.5
precioF = total_litros * precio
tiempo = distancia / 90


print(f"Para todo el viaje nesesitará un total de: ${precioF}, ya que gastará {total_litros} litros en todo el viaje")
print(f"Si la velocidad se mantiene en un promedio de 90km/h, el viaje durará {tiempo} horas aprox")


print("-------------------------------------------------------------------")

#EJERCICIO 9: PRÉSTAMO BANCARIO

prestamo = float(input("Ingrese el monto del préstamo solicitado: "))
interes = 1.02
meses = 12

interes_total = prestamo * interes * meses 

devolver = prestamo + interes_total 

cuota = interes_total / meses 

print(f"El monto total a devolver por su prestamo de: ${prestamo} pesos, es de: ${devolver} pesos")
print(f"El valor de las cuotas será de: ${cuota} pesos")