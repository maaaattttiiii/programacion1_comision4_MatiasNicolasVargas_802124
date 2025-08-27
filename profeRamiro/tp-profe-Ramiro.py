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


