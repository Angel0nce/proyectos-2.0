import os
from datetime import datetime

def ListarArchivos():
    """Muestra los archivos .txt disponibles en el directorio actual."""
    print("\nArchivos disponibles en el directorio actual:")
    archivos = [archivo for archivo in os.listdir() if archivo.endswith(".txt")]
    if archivos:
        for idx, archivo in enumerate(archivos, start=1):
            print(f"{idx}. {archivo}")
        return archivos
    else:
        print("No se encontraron archivos .txt en el directorio.")
        return []

def SeleccionarArchivo():
    """Permite al usuario seleccionar un archivo de la lista."""
    archivos = ListarArchivos()
    if archivos:
        while True:
            try:
                opcion = int(input("\nElige el número del archivo que deseas seleccionar: ")) - 1
                if 0 <= opcion < len(archivos):
                    print(f"Has seleccionado el archivo: {archivos[opcion]}")
                    return archivos[opcion]
                else:
                    print("Número fuera de rango. Inténtalo nuevamente.")
            except ValueError:
                print("Por favor, introduce un número válido.")
    return None

def CreadorArchivo():
    fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    NomArchivo = input("Introduce el nombre del Archivo:\n> ")
    nombre_archivo = f"{NomArchivo} {fecha_actual}.txt"

    with open(nombre_archivo, "w") as archivo:
        archivo.write(f"Inventario del día - Generado el {datetime.now().strftime('%d/%m/%Y a las %H:%M:%S')}\n")
        archivo.write("Producto | Precio | Cantidad\n")
        archivo.write("-" * 30 + "\n")
    print(f"Archivo de Inventario generado con éxito: {nombre_archivo}")
    return nombre_archivo

def AgregarProductos(nombre_archivo):
    print(f"\nAbriendo archivo '{nombre_archivo}' para agregar productos...")
    with open(nombre_archivo, "a") as archivo:
        while True:
            print("\nIngrese los datos del producto:")
            producto = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad en stock: "))

            archivo.write(f"{producto} | {precio:.2f} | {cantidad}\n")

            continuar = input("¿Desea agregar otro producto? (s/n): ").lower()
            if continuar != 's':
                break
    print(f"Productos añadidos al archivo '{nombre_archivo}' con éxito.")

def VerArchivo(nombre_archivo):
    print(f"\nMostrando el contenido del archivo '{nombre_archivo}':")
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print("\n" + contenido)
    except FileNotFoundError:
        print("El archivo no existe. Por favor, selecciona un archivo válido.")

def Menu():
    nombre_archivo = None

    while True:
        print("""
        Menú de Inventario:
        1. Crear un nuevo archivo de inventario
        2. Seleccionar un archivo existente
        3. Agregar productos al archivo seleccionado
        4. Ver contenido del archivo seleccionado
        5. Salir
        """)

        opcion = input("> ")
        if opcion == "1":
            nombre_archivo = CreadorArchivo()
        elif opcion == "2":
            nombre_archivo = SeleccionarArchivo()
        elif opcion == "3":
            if nombre_archivo:
                AgregarProductos(nombre_archivo)
            else:
                print("Primero debes seleccionar o crear un archivo.")
        elif opcion == "4":
            if nombre_archivo:
                VerArchivo(nombre_archivo)
            else:
                print("Primero debes seleccionar o crear un archivo.")
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

# Iniciar el programa
Menu()


    



   




        

   



  

   

                      




























