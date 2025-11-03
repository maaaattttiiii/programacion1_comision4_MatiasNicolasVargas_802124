import csv
import os 

def cargar_csv(ruta_archivo):
    herramientas = []
    if not os.path.exists(ruta_archivo):
        return herramientas
    try:
        with open(ruta_archivo, mode="r", encoding="utf-8")as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    herramienta = {
                        "nombre" : fila["nombre"],
                        "stock" : int(fila["stock"]),
                        "precio" : float(fila["precio"])}
                    herramientas.append(herramienta)
                except(ValueError, KeyError):
                    print(f"ERROR al leer la fila, {fila} , se omite")
    except Exception as e:
        print(f"ERROR al cargar el archivo: {e}")
    return herramientas

def guardar_en_csv(herramientas, ruta_archivo):
    try:
        with open(ruta_archivo, mode="w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "stock", "precio"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(herramientas)
    except Exception as e:
        print(f"ERROR al guardar el archivo csv: {e}")

def cargar_herramienta(herramientas, ruta_archivo):
    nombre = input("Ingrese nombre: ").strip()
    if not nombre:
        print(" El nombre no puede estar vacío.")
        return

    # Validación de stock
    while True:
        try:
            stock = int(input("Ingrese stock: "))
            if stock < 0:
                raise ValueError
            break
        except ValueError:
            print(" Ingrese un número entero válido (0 o mayor).")

    # Validación de precio
    while True:
        try:
            precio = float(input("Ingrese precio: "))
            if precio < 0:
                raise ValueError
            break
        except ValueError:
            print(" Ingrese un precio numérico válido (mayor o igual a 0).")

    herramienta = {"nombre": nombre, "stock": stock, "precio": precio}
    herramientas.append(herramienta)
    guardar_en_csv(herramientas, ruta_archivo)
    print(" Herramienta registrada correctamente.")


def mostrar_herramientas(herramientas):
    if not herramientas:
        print("No hay herramientas registradas.")
        return
    print("\n--- Inventario Actual ---")
    for h in herramientas:
        print(f"{h['nombre']} → Stock: {h['stock']} → Precio: ${h['precio']:.2f}")
    print("---------------------------")


def modificar_herramienta(herramientas, ruta_archivo):
    nombre = input("Ingrese el nombre de la herramienta a modificar: ").strip()
    for h in herramientas:
        if h["nombre"].lower() == nombre.lower():
            try:
                nuevo_stock = int(input("Nuevo stock: "))
                nuevo_precio = float(input("Nuevo precio: "))
                if nuevo_stock < 0 or nuevo_precio < 0:
                    print(" Los valores deben ser positivos.")
                    return
                h["stock"] = nuevo_stock
                h["precio"] = nuevo_precio
                guardar_en_csv(herramientas, ruta_archivo)
                print(" Datos actualizados correctamente.")
                return
            except ValueError:
                print("Error: el stock y el precio deben ser números.")
                return
    print(" Herramienta no encontrada.")


def eliminar_herramienta(herramientas, ruta_archivo):
    nombre = input("Ingrese el nombre de la herramienta a eliminar: ").strip()
    for h in herramientas:
        if h["nombre"].lower() == nombre.lower():
            herramientas.remove(h)
            guardar_en_csv(herramientas, ruta_archivo)
            print(" Herramienta eliminada correctamente.")
            return
    print(" No se encontró la herramienta especificada.")


def consultar_disponibilidad(herramientas):
    nombre = input("Ingrese el nombre de la herramienta: ").strip()
    for h in herramientas:
        if h["nombre"].lower() == nombre.lower():
            print(f"{h['nombre']} → Stock disponible: {h['stock']} unidades.")
            return
    print(" Herramienta no encontrada.")


def listar_sin_stock(herramientas):
    sin_stock = [h for h in herramientas if h["stock"] == 0]
    if not sin_stock:
        print("No hay herramientas sin stock.")
    else:
        print("\n--- Herramientas sin stock ---")
        for h in sin_stock:
            print(f"{h['nombre']} (Precio: ${h['precio']:.2f})")
        print("-------------------------------")

def buscar_por_precio(herramientas):
    try:
        limite = float(input("Mostrar herramientas con precio mayor a: $"))
        resultados = [h for h in herramientas if h["precio"] > limite]
        if resultados:
            print(f"\n--- Herramientas con precio mayor a ${limite:.2f} ---")
            for h in resultados:
                print(f"{h['nombre']} → ${h['precio']:.2f}")
        else:
            print(f"No hay herramientas con precio mayor a ${limite:.2f}.")
    except ValueError:
        print(" Ingrese un valor numérico válido.")
    

def main():

    archivo_csv = "inventario.csv"
    herramientas = cargar_csv(archivo_csv)
    while True:
        print("\n====== MENÚ FERRETERÍA ======")
        print("1. Cargar herramienta")
        print("2. Mostrar herramientas")
        print("3. Modificar herramienta")
        print("4. Eliminar herramienta")
        print("5. Consultar disponibilidad")
        print("6. Listar sin stock")
        print("7. Buscar por precio (extra)")
        print("8. Salir")
        print("==============================")

        opcion = input("Seleccione una opción (1-8): ").strip()

        if opcion == "1":
            cargar_herramienta(herramientas, archivo_csv)
        elif opcion == "2":
            mostrar_herramientas(herramientas)
        elif opcion == "3":
            modificar_herramienta(herramientas, archivo_csv)
        elif opcion == "4":
            eliminar_herramienta(herramientas, archivo_csv)
        elif opcion == "5":
            consultar_disponibilidad(herramientas)
        elif opcion == "6":
            listar_sin_stock(herramientas)
        elif opcion == "7":
            buscar_por_precio(herramientas)
        elif opcion == "8":
            guardar_en_csv(herramientas, archivo_csv)
            print(" Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print(" Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
    