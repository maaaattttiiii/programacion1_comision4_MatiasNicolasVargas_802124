print("\n BIENVENIDO AL PROGRAMA DE ADMINISTRACION DEL KIOSCO YES")

import csv
import os

# === Nombre del archivo CSV ===
ARCHIVO = "productos.csv"


# === Función para verificar o crear el archivo si no existe ===
def verificar_archivo():
    """Crea el archivo CSV con encabezados si no existe."""
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, mode="w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=["nombre", "precio"])
            escritor.writeheader()


# === Función para leer todos los productos ===
def leer_productos():
    """Lee los productos desde el archivo CSV y los devuelve en una lista de diccionarios."""
    productos = []
    try:
        with open(ARCHIVO, mode="r", newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                productos.append({"nombre": fila["nombre"], "precio": float(fila["precio"])})
    except FileNotFoundError:
        print("El archivo no existe. Se creará automáticamente.")
        verificar_archivo()
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return productos


# === Función para mostrar los productos ===
def mostrar_productos():
    """Muestra todos los productos registrados con su precio y el total acumulado."""
    productos = leer_productos()
    if not productos:
        print("\nNo hay productos registrados.\n")
        return

    print("\n=== LISTA DE PRODUCTOS ===")
    total = 0
    for p in productos:
        print(f"- {p['nombre']} | ${p['precio']:.2f}")
        total += p["precio"]

    print(f"\nTOTAL ACUMULADO: ${total:.2f}\n")


# === Función para agregar un producto ===
def agregar_producto():
    """Agrega un nuevo producto al archivo CSV."""
    nombre = input("Ingrese el nombre del producto: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio <= 0:
            print("El precio debe ser un número positivo.")
            return
    except ValueError:
        print("Debe ingresar un valor numérico válido para el precio.")
        return

    with open(ARCHIVO, mode="a", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["nombre", "precio"])
        escritor.writerow({"nombre": nombre, "precio": precio})

    print(f"Producto '{nombre}' agregado correctamente.\n")


# === Función para eliminar un producto ===
def eliminar_producto():
    """Elimina un producto existente por nombre."""
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
    productos = leer_productos()
    encontrado = False

    nuevos_productos = [p for p in productos if p["nombre"].lower() != nombre.lower()]

    if len(nuevos_productos) != len(productos):
        encontrado = True
        with open(ARCHIVO, mode="w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=["nombre", "precio"])
            escritor.writeheader()
            escritor.writerows(nuevos_productos)
        print(f"Producto '{nombre}' eliminado correctamente.\n")
    else:
        print(f"No se encontró el producto '{nombre}'.\n")


# === Función principal con el menú ===
def menu():
    """Muestra el menú principal y gestiona las opciones del usuario."""
    verificar_archivo()

    while True:
        print("====== MENÚ DE PRODUCTOS ======")
        print("1. Mostrar productos")
        print("2. Agregar producto")
        print("3. Eliminar producto")
        print("4. Salir")
        print("===============================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            print("Saliendo del programa... ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")


# === Ejecución del programa ===
if __name__ == "__main__":
    menu()
