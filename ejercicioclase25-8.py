fin = False

# PEDIMOS LA FECHA 

fecha = input("Ingrese la fecha actual (día, DD/MM): ")

#SEPARAR LA FECHA 

partes = fecha.split(",")
if len(partes) != 2:
    print("ERROR, respetar formato de fecha pedido")
    fin = True
dia_semana= partes[0].strip().lower()

fecha_num = partes[1].strip()
partes_fecha= fecha_num.split("/")
if len(partes_fecha) != 2:
    print("ERROR, respetar formato de fecha pedido")
    fin = True

dd = int(partes_fecha[0])
mm = int(partes_fecha[1])

#VERIFICAMOS PARA LOS ERRORES 

if dd > 31 or mm > 12 or dd < 1 or mm < 1: 
    print("ERROR, ingrese valores válidos")
    fin = True 

#LISTA PARA LOS NIVELES

niveles = { "lunes" : "inicial",
 "martes" : "intermedio",
  "miercoles" : "avanzado",
  "miércoles" : "avanzado",
 "jueves" : "prácticas habladas",
 "viernes" : "viajeros",
 }

if dia_semana not in niveles: 
    print ("ERROR, el día ingresado no es válido")
    fin = True

#ASIGNAR NIVEL

if fin == False: 
    nivel = niveles[dia_semana]
    print (f"Hoy es {dia_semana} , el nivel del alumno es: {nivel}")

#INDICAR SI HAY EXAMENES O NO 

if fin == False: 
    if dia_semana == "lunes":
        examen = input(str("¿Hubo examen?(S/N)"))
        examen = examen.lower()
        if examen not in ("s" , "n"):
            fin = True 
            print ("Ingrese un valor válido")
        elif examen == "s":
            print ("Ingrese numero de aprobados y desaprobados a continuación")
            aprobados = int(input("APROBADOS: "))
            desaprobados = int(input("DESAPROBADOS: "))
            total = aprobados + desaprobados
            porcentaje = aprobados / total 
            print(f"El porcentaje de aprobados es: ", {porcentaje})
        else:
            print ("No hubo examen")
    elif dia_semana == "martes":
        examen = input(str("¿Hubo examen?(S/N)"))
        examen = examen.lower()
        if examen not in ("s" , "n"):
            fin = True 
            print ("Ingrese un valor válido")
        elif examen == "s":
            print ("Ingrese numero de aprobados y desaprobados a continuación")
            aprobados = int(input("APROBADOS: "))
            desaprobados = int(input("DESAPROBADOS: "))
            total = aprobados + desaprobados
            porcentaje = aprobados / total 
            print(f"El porcentaje de aprobados es: ", {porcentaje})
        else:
            print ("No hubo examen")
    elif dia_semana == "miercoles":
        examen = input(str("¿Hubo examen?(S/N)"))
        examen = examen.lower()
        if examen not in ("s" , "n"):
            fin = True 
            print ("Ingrese un valor válido")
        elif examen == "s":
            print ("Ingrese numero de aprobados y desaprobados a continuación")
            aprobados = int(input("APROBADOS: "))
            desaprobados = int(input("DESAPROBADOS: "))
            total = aprobados + desaprobados
            porcentaje = aprobados / total 
            print(f"El porcentaje de aprobados es: ", {porcentaje})
        else:
            print ("No hubo examen")
    elif dia_semana == "miércoles": 
        examen = input(str("¿Hubo examen?(S/N)"))
        examen = examen.lower()
        if examen not in ("s" , "n"):
            fin = True 
            print ("Ingrese un valor válido")
        elif examen == "s":
            print ("Ingrese numero de aprobados y desaprobados a continuación")
            aprobados = int(input("APROBADOS: "))
            desaprobados = int(input("DESAPROBADOS: "))
            total = aprobados + desaprobados
            porcentaje = aprobados / total 
            print(f"El porcentaje de aprobados es: ", {porcentaje})
        else:
            print ("No hubo examen")
    elif dia_semana == "jueves":
        print ("Jueves fue dia de práctica hablada")
        asistencia = int(input("Indique el porcentaje de asistencia: %"))
        if asistencia > 50 < 100: 
            print ("Asistió la mayoría")
        elif asistencia >= 1 <= 50 :
            print ("No asistió la mayoría")
        else : 
            print ("Ingrese un porcentaje válido")
    elif dia_semana == "viernes":
        if dd == 1 and mm == 1 or mm == 7: 
            print ("Comienzo de nuevo ciclo")
            nuevos = int(input("Ingrese cuantos alumnos nuevos hay: "))
            valor = int(input("Ingrese el valor de la cuota por cada alumno: "))
            print(f"El ingreso total sería de: ${nuevos}*{valor}")
        else: 
            print( f"Hoy es, {dia_semana}, el día de ingles para viajeros")
    else: 
        print("Error, el valor ingresado no es válido")

    




