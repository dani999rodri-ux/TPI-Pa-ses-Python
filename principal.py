import csv
import os

# =====================================
# CREAR CSV SI NO EXISTE
# =====================================

def crear_csv():

    if not os.path.exists("paises.csv"):

        with open(
            "paises.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as archivo:

            escritor = csv.writer(archivo)

            escritor.writerow([
                "nombre",
                "poblacion",
                "superficie",
                "continente"
            ])

# =====================================
# CARGAR PAISES
# =====================================

def cargar_paises():

    paises = []

    try:

        with open(
            "paises.csv",
            "r",
            encoding="utf-8"
        ) as archivo:

            lector = csv.DictReader(archivo)

            for fila in lector:

                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }

                paises.append(pais)

    except Exception as e:
        print("Error:", e)

    return paises

# =====================================
# GUARDAR PAISES
# =====================================

def guardar_paises(lista):

    with open(
        "paises.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as archivo:

        campos = [
            "nombre",
            "poblacion",
            "superficie",
            "continente"
        ]

        escritor = csv.DictWriter(
            archivo,
            fieldnames=campos
        )

        escritor.writeheader()

        escritor.writerows(lista)

# =====================================
# MOSTRAR PAISES
# =====================================

def mostrar_paises(lista):

    if len(lista) == 0:
        print("\nNo hay países.")
        return

    for pais in lista:

        print("\n-------------------")
        print("Nombre:", pais["nombre"])
        print("Población:", pais["poblacion"])
        print("Superficie:", pais["superficie"])
        print("Continente:", pais["continente"])

# =====================================
# AGREGAR PAIS
# =====================================

def agregar_pais(lista):

    nombre = input("Nombre: ").strip()

    if nombre == "":
        print("Nombre inválido.")
        return

    try:

        poblacion = int(
            input("Población: ")
        )

        superficie = int(
            input("Superficie: ")
        )

    except ValueError:

        print("Debe ingresar números.")
        return

    continente = input(
        "Continente: "
    ).strip()

    nuevo = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    lista.append(nuevo)

    guardar_paises(lista)

    print("\nPaís agregado correctamente.")

# =====================================
# ACTUALIZAR PAIS
# =====================================

def actualizar_pais(lista):

    nombre = input(
        "País a actualizar: "
    )

    for pais in lista:

        if pais["nombre"].lower() == nombre.lower():

            try:

                pais["poblacion"] = int(
                    input("Nueva población: ")
                )

                pais["superficie"] = int(
                    input("Nueva superficie: ")
                )

            except ValueError:

                print("Error.")
                return

            guardar_paises(lista)

            print("Actualizado.")

            return

    print("País no encontrado.")

# =====================================
# BUSCAR PAIS
# =====================================

def buscar_pais(lista):

    texto = input(
        "Ingrese nombre: "
    )

    encontrados = []

    for pais in lista:

        if texto.lower() in pais["nombre"].lower():

            encontrados.append(pais)

    mostrar_paises(encontrados)

# =====================================
# FILTRAR CONTINENTE
# =====================================

def filtrar_continente(lista):

    continente = input(
        "Continente: "
    )

    resultado = []

    for pais in lista:

        if pais["continente"].lower() == continente.lower():

            resultado.append(pais)

    mostrar_paises(resultado)

# =====================================
# FILTRAR POBLACION
# =====================================

def filtrar_poblacion(lista):

    minimo = int(
        input("Mínimo: ")
    )

    maximo = int(
        input("Máximo: ")
    )

    resultado = []

    for pais in lista:

        if minimo <= pais["poblacion"] <= maximo:

            resultado.append(pais)

    mostrar_paises(resultado)

# =====================================
# FILTRAR SUPERFICIE
# =====================================

def filtrar_superficie(lista):

    minimo = int(
        input("Mínimo: ")
    )

    maximo = int(
        input("Máximo: ")
    )

    resultado = []

    for pais in lista:

        if minimo <= pais["superficie"] <= maximo:

            resultado.append(pais)

    mostrar_paises(resultado)

# =====================================
# ORDENAR
# =====================================

def ordenar_paises(lista):

    print("\n1-Nombre")
    print("2-Población")
    print("3-Superficie")

    opcion = input("Opción: ")

    orden = input(
        "A=Ascendente D=Descendente: "
    ).upper()

    reverse = orden == "D"

    if opcion == "1":

        ordenados = sorted(
            lista,
            key=lambda x: x["nombre"],
            reverse=reverse
        )

    elif opcion == "2":

        ordenados = sorted(
            lista,
            key=lambda x: x["poblacion"],
            reverse=reverse
        )

    elif opcion == "3":

        ordenados = sorted(
            lista,
            key=lambda x: x["superficie"],
            reverse=reverse
        )

    else:

        print("Opción inválida.")
        return

    mostrar_paises(ordenados)

# =====================================
# ESTADISTICAS
# =====================================

def estadisticas(lista):

    if len(lista) == 0:

        print("Sin datos.")
        return

    mayor = max(
        lista,
        key=lambda x: x["poblacion"]
    )

    menor = min(
        lista,
        key=lambda x: x["poblacion"]
    )

    promedio_poblacion = (
        sum(
            pais["poblacion"]
            for pais in lista
        ) / len(lista)
    )

    promedio_superficie = (
        sum(
            pais["superficie"]
            for pais in lista
        ) / len(lista)
    )

    print("\n===== ESTADÍSTICAS =====")

    print(
        "Mayor población:",
        mayor["nombre"]
    )

    print(
        "Menor población:",
        menor["nombre"]
    )

    print(
        "Promedio población:",
        round(promedio_poblacion, 2)
    )

    print(
        "Promedio superficie:",
        round(promedio_superficie, 2)
    )

    continentes = {}

    for pais in lista:

        cont = pais["continente"]

        if cont in continentes:

            continentes[cont] += 1

        else:

            continentes[cont] = 1

    print("\nPaíses por continente:")

    for cont, cantidad in continentes.items():

        print(cont, ":", cantidad)

# =====================================
# MENU
# =====================================

def menu():

    crear_csv()

    paises = cargar_paises()

    while True:

        print("\n===== MENÚ =====")
        print("1. Mostrar países")
        print("2. Agregar país")
        print("3. Actualizar país")
        print("4. Buscar país")
        print("5. Filtrar continente")
        print("6. Filtrar población")
        print("7. Filtrar superficie")
        print("8. Ordenar")
        print("9. Estadísticas")
        print("0. Salir")

        opcion = input(
            "Seleccione opción: "
        )

        if opcion == "1":
            mostrar_paises(paises)

        elif opcion == "2":
            agregar_pais(paises)

        elif opcion == "3":
            actualizar_pais(paises)

        elif opcion == "4":
            buscar_pais(paises)

        elif opcion == "5":
            filtrar_continente(paises)

        elif opcion == "6":
            filtrar_poblacion(paises)

        elif opcion == "7":
            filtrar_superficie(paises)

        elif opcion == "8":
            ordenar_paises(paises)

        elif opcion == "9":
            estadisticas(paises)

        elif opcion == "0":

            print("Programa finalizado.")
            break

        else:

            print("Opción inválida.")

# =====================================
# INICIO
# =====================================

menu()
