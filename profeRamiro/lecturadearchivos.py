ruta = r"C:\Users\mativ\OneDrive\Documentos\MATI FACULAD\SEMESTRE 1\PROGRAMACION UNO\listaAlumnosC4.txt"
archivo = open(ruta,"r",encoding="utf-8")

print("CONTENIDO DE EL ARCHIVO\n")

for linea in archivo:
        nombre = linea.split(",") 
        print(nombre)
