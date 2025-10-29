#!/usr/bin/env python3
# Trabajo Práctico Integrador - Programación 1
# Gestión de Datos de Países usando una API
# Autor: (tu nombre)
# Objetivo: aplicar listas, diccionarios, funciones, condicionales,
# ordenamientos, estadísticas y manejo de errores.
# Fuente de datos: https://restcountries.com/v3.1/all

import requests
from collections import Counter
from typing import List, Dict, Optional
import sys

# Tipo de dato para representar un país
Country = Dict[str, object]

# ----------------------------------------------------------------------
# 1) Cargar países desde la API
# ----------------------------------------------------------------------
def load_countries_from_api() -> (List[Country], List[str]):
    """
    Obtiene datos de la API 'restcountries.com' y los adapta al formato usado en el TPI.
    Cada país tendrá: nombre, población, superficie (área) y continente.
    """
    url = "https://github.com/arr1790/Paises-del-Mundo.git"
    countries = []
    errors = []
    try:
        print("Conectando a la API, por favor espere...")
        response = requests.get(url, timeout=15)
        if response.status_code != 200:
            errors.append(f"Error HTTP {response.status_code}")
            return [], errors

        data = response.json()
        for c in data:
            try:
                nombre = c.get("name", {}).get("common", "Desconocido")
                poblacion = int(c.get("population", 0))
                superficie = int(c.get("area", 0)) if c.get("area") else 0
                continente = c.get("region", "Desconocido")
                countries.append({
                    "nombre": nombre,
                    "poblacion": poblacion,
                    "superficie": superficie,
                    "continente": continente
                })
            except Exception as e:
                errors.append(f"Error al procesar país: {e}")
    except requests.exceptions.RequestException as e:
        errors.append(f"Error al conectar con la API: {e}")

    return countries, errors

# ----------------------------------------------------------------------
# 2) Funciones de búsqueda y filtrado
# ----------------------------------------------------------------------
def search_by_name(countries: List[Country], query: str) -> List[Country]:
    q = query.strip().lower()
    return [c for c in countries if q in c["nombre"].lower()]

def filter_by_continent(countries: List[Country], continent: str) -> List[Country]:
    c = continent.strip().lower()
    return [country for country in countries if country["continente"].lower() == c]

def filter_by_population_range(countries: List[Country], min_pop: Optional[int], max_pop: Optional[int]) -> List[Country]:
    return [
        c for c in countries
        if (min_pop is None or c["poblacion"] >= min_pop)
        and (max_pop is None or c["poblacion"] <= max_pop)
    ]

def filter_by_surface_range(countries: List[Country], min_surf: Optional[int], max_surf: Optional[int]) -> List[Country]:
    return [
        c for c in countries
        if (min_surf is None or c["superficie"] >= min_surf)
        and (max_surf is None or c["superficie"] <= max_surf)
    ]

# ----------------------------------------------------------------------
# 3) Ordenamientos
# ----------------------------------------------------------------------
def sort_countries(countries: List[Country], key_field: str, reverse: bool = False) -> List[Country]:
    if key_field not in ("nombre", "poblacion", "superficie"):
        raise ValueError("Campo inválido para ordenamiento.")
    return sorted(countries, key=lambda x: x[key_field], reverse=reverse)

# ----------------------------------------------------------------------
# 4) Estadísticas
# ----------------------------------------------------------------------
def country_with_max_population(countries: List[Country]) -> Optional[Country]:
    return max(countries, key=lambda c: c["poblacion"], default=None)

def country_with_min_population(countries: List[Country]) -> Optional[Country]:
    return min(countries, key=lambda c: c["poblacion"], default=None)

def average_population(countries: List[Country]) -> Optional[float]:
    if not countries:
        return None
    return sum(c["poblacion"] for c in countries) / len(countries)

def average_surface(countries: List[Country]) -> Optional[float]:
    if not countries:
        return None
    return sum(c["superficie"] for c in countries) / len(countries)

def count_by_continent(countries: List[Country]) -> Dict[str, int]:
    conts = [c["continente"] for c in countries]
    return dict(Counter(conts))

# ----------------------------------------------------------------------
# 5) Utilidades de impresión
# ----------------------------------------------------------------------
def print_country(c: Country) -> None:
    print(f"{c['nombre']:<30} | Población: {c['poblacion']:<12} | Superficie: {c['superficie']:<10} km² | Continente: {c['continente']}")

def print_countries_list(lst: List[Country]) -> None:
    if not lst:
        print("No se encontraron países.")
        return
    for c in lst:
        print_country(c)

def safe_input_int(prompt: str) -> Optional[int]:
    s = input(prompt).strip()
    if s == "":
        return None
    try:
        return int(s)
    except ValueError:
        print("Entrada inválida. Se tomará como vacío.")
        return None

# ----------------------------------------------------------------------
# 6) Menú principal
# ----------------------------------------------------------------------
def main_menu(countries: List[Country]) -> None:
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1) Buscar país por nombre")
        print("2) Filtrar por continente")
        print("3) Filtrar por rango de población")
        print("4) Filtrar por rango de superficie")
        print("5) Ordenar países")
        print("6) Mostrar estadísticas")
        print("7) Mostrar todos los países")
        print("0) Salir")
        op = input("Seleccione una opción: ").strip()
        if op == "1":
            q = input("Ingrese nombre o parte del nombre: ")
            res = search_by_name(countries, q)
            print_countries_list(res)
        elif op == "2":
            cont = input("Ingrese continente (Ej: Europe, Asia, Americas, Africa, Oceania): ")
            res = filter_by_continent(countries, cont)
            print_countries_list(res)
        elif op == "3":
            mi = safe_input_int("Población mínima: ")
            ma = safe_input_int("Población máxima: ")
            res = filter_by_population_range(countries, mi, ma)
            print_countries_list(res)
        elif op == "4":
            mi = safe_input_int("Superficie mínima (km²): ")
            ma = safe_input_int("Superficie máxima (km²): ")
            res = filter_by_surface_range(countries, mi, ma)
            print_countries_list(res)
        elif op == "5":
            print("1) Nombre  2) Población  3) Superficie")
            field = input("Campo: ").strip()
            mapping = {"1": "nombre", "2": "poblacion", "3": "superficie"}
            if field not in mapping:
                print("Campo inválido.")
                continue
            reverse = input("¿Descendente? (s/n): ").lower().startswith("s")
            ordenado = sort_countries(countries, mapping[field], reverse)
            print_countries_list(ordenado)
        elif op == "6":
            mx = country_with_max_population(countries)
            mn = country_with_min_population(countries)
            avgp = average_population(countries)
            avga = average_surface(countries)
            conts = count_by_continent(countries)
            print("\n=== ESTADÍSTICAS ===")
            if mx:
                print(f"País con mayor población: {mx['nombre']} ({mx['poblacion']})")
            if mn:
                print(f"País con menor población: {mn['nombre']} ({mn['poblacion']})")
            if avgp:
                print(f"Promedio de población: {avgp:,.0f}")
            if avga:
                print(f"Promedio de superficie: {avga:,.0f} km²")
            print("Cantidad de países por continente:")
            for k, v in conts.items():
                print(f"  {k}: {v}")
        elif op == "7":
            print_countries_list(countries)
        elif op == "0":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente nuevamente.")

# ----------------------------------------------------------------------
# 7) Ejecución principal
# ----------------------------------------------------------------------
def main():
    countries, errors = load_countries_from_api()
    if errors:
        print("⚠️ Errores detectados:")
        for e in errors:
            print(" -", e)
    print(f"✅ Se cargaron {len(countries)} países desde la API.")
    main_menu(countries)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupción por teclado. Saliendo.")
        sys.exit(0)



