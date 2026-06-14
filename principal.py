import csv

# =========================
# CARGAR DATOS DESDE CSV
# =========================
def cargar_paises(nombre_archivo):
    paises = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }
                paises.append(pais)
    except FileNotFoundError:
        print("Error: No se encontró el archivo CSV.")
    except Exception as e:
        print("Error al cargar datos:", e)

    return paises


# =========================
# GUARDAR DATOS EN CSV (Función nueva para automatizar)
# =========================
def guardar_paises(nombre_archivo, lista_paises):
    try:
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            # Escribe la primera fila con los nombres de las columnas
            escritor.writeheader()
            # Escribe todas las filas de nuestra lista
            escritor.writerows(lista_paises)
    except Exception as e:
        print("Error al guardar en el archivo CSV:", e)


# =========================
# MOSTRAR PAISES
# =========================
def mostrar_paises(lista):
    if not lista:
        print("No hay países para mostrar.")
        return

    for pais in lista:
        print("-" * 50)
        print("Nombre:", pais["nombre"])
        print("Población:", pais["poblacion"])
        print("Superficie:", pais["superficie"])
        print("Continente:", pais["continente"])


# =========================
# AGREGAR PAIS
# =========================
def agregar_pais(lista):
    nombre = input("Nombre del país: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    try:
        poblacion = int(input("Población: "))
        superficie = int(input("Superficie km²: "))
    except ValueError:
        print("Debe ingresar números válidos.")
        return

    continente = input("Continente: ").strip()

    if continente == "":
        print("El continente no puede estar vacío.")
        return

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    # Agrega a la memoria
    lista.append(nuevo_pais)
    
    # ¡GUARDADO AUTOMÁTICO! Guarda la lista entera actualizada en el archivo
    guardar_paises("paises.csv", lista)

    print("País agregado y guardado en CSV correctamente.")


# =========================
# ACTUALIZAR PAIS
# =========================
def actualizar_pais(lista):
    nombre = input("Ingrese país a actualizar: ")

    for pais in lista:
        if pais["nombre"].lower() == nombre.lower():
            try:
                pais["poblacion"] = int(input("Nueva población: "))
                pais["superficie"] = int(input("Nueva superficie: "))
            except ValueError:
                print("Datos inválidos.")
                return

            # ¡GUARDADO AUTOMÁTICO! Como modificamos un dato en memoria, lo impactamos en el archivo
            guardar_paises("paises.csv", lista)
            print("País actualizado y guardado en CSV correctamente.")
            return

    print("País no encontrado.")


# =========================
# BUSCAR PAIS
# =========================
def buscar_pais(lista):
    texto = input("Ingrese nombre o parte del nombre: ")
    encontrados = []

    for pais in lista:
        if texto.lower() in pais["nombre"].lower():
            encontrados.append(pais)

    if encontrados:
        mostrar_paises(encontrados)
    else:
        print("No se encontraron coincidencias.")


# =========================
# FILTRAR CONTINENTE
# =========================
def filtrar_continente(lista):
    continente = input("Continente: ")
    resultado = []

    for pais in lista:
        if pais["continente"].lower() == continente.lower():
            resultado.append(pais)

    mostrar_paises(resultado)


# =========================
# FILTRAR POBLACION
# =========================
def filtrar_poblacion(lista):
    try:
        minimo = int(input("Población mínima: "))
        maximo = int(input("Población máxima: "))
    except ValueError:
        print("Debe ingresar números.")
        return

    resultado = []

    for pais in lista:
        if minimo <= pais["poblacion"] <= maximo:
            resultado.append(pais)

    mostrar_paises(resultado)


# =========================
# FILTRAR SUPERFICIE
# =========================
def filtrar_superficie(lista):
    try:
        minimo = int(input("Superficie mínima: "))
        maximo = int(input("Superficie máxima: "))
    except ValueError:
        print("Debe ingresar números.")
        return

    resultado = []

    for pais in lista:
        if minimo <= pais["superficie"] <= maximo:
            resultado.append(pais)

    mostrar_paises(resultado)


# =========================
# ORDENAMIENTOS
# =========================
def ordenar_paises(lista):
    print("\n1. Nombre")
    print("2. Población")
    print("3. Superficie")

    opcion = input("Seleccione criterio: ")
    orden = input("Ascendente(A) / Descendente(D): ").upper()
    reverse = orden == "D"

    if opcion == "1":
        ordenados = sorted(lista, key=lambda x: x["nombre"], reverse=reverse)
    elif opcion == "2":
        ordenados = sorted(lista, key=lambda x: x["poblacion"], reverse=reverse)
    elif opcion == "3":
        ordenados = sorted(lista, key=lambda x: x["superficie"], reverse=reverse)
    else:
        print("Opción inválida.")
        return

    mostrar_paises(ordenados)


# =========================
# ESTADISTICAS
# =========================
def mostrar_estadisticas(lista):
    if len(lista) == 0:
        print("No hay datos.")
        return

    mayor_pob = max(lista, key=lambda x: x["poblacion"])
    menor_pob = min(lista, key=lambda x: x["poblacion"])

    promedio_pob = sum(p["poblacion"] for p in lista) / len(lista)
    promedio_sup = sum(p["superficie"] for p in lista) / len(lista)

    continentes = {}
    for pais in lista:
        cont = pais["continente"]
        if cont in continentes:
            continentes[cont] += 1
        else:
            continentes[cont] = 1

    print("\n===== ESTADÍSTICAS =====")
    print("Mayor población:", mayor_pob["nombre"], mayor_pob["poblacion"])
    print("Menor población:", menor_pob["nombre"], menor_pob["poblacion"])
    print("Promedio población:", round(promedio_pob, 2))
    print("Promedio superficie:", round(promedio_sup, 2))

    print("\nCantidad por continente:")
    for continente, cantidad in continentes.items():
        print(continente, ":", cantidad)


# =========================
# MENU PRINCIPAL
# =========================
def menu():
    paises = cargar_paises("paises.csv")

    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Mostrar países")
        print("2. Agregar país")
        print("3. Actualizar país")
        print("4. Buscar país")
        print("5. Filtrar por continente")
        print("6. Filtrar por población")
        print("7. Filtrar por superficie")
        print("8. Ordenar países")
        print("9. Estadísticas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

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
            mostrar_estadisticas(paises)
        elif opcion == "0":
            print("Fin del programa.")
            break
        else:
            print("Opción inválida.")


# =========================
# INICIO
# =========================
menu()
