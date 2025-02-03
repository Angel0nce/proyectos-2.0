from datetime import datetime

def generar_reporte():
    """Genera un archivo de gastos con un título inicial."""
    print("Generando archivo de gastos...")
    with open("Gastos.txt", "w") as archivo:
        archivo.write("Reporte de gastos\n")
    print("Archivo de gastos generado con éxito.")


def editar_reporte():
    """Abre el archivo de gastos y permite agregar datos nuevos."""
    print("Abriendo archivo de gastos para edición...")
    try:
        with open("Gastos.txt", "a") as archivo:
            print("Introduce los gastos del día (por ejemplo, 'Comida: 50, Transporte: 20').")
            gastos = input("Gastos: ")
            archivo.write(f"Gastos del día: {gastos}\n")
        print("Cambios guardados correctamente.")
    except FileNotFoundError:
        print("El archivo 'Gastos.txt' no existe. Por favor, genera el reporte primero.")


def main():
    """Función principal para mostrar el menú y ejecutar las opciones."""
    while True:
        print("""
Introduce la opción que deseas realizar: 
1 - Generar un reporte de gastos
2 - Editar reporte de gastos
3 - Salir del programa
        """)
        try:
            opcion = int(input("> "))
            if opcion == 1:
                generar_reporte()
            elif opcion == 2:
                editar_reporte()
            elif opcion == 3:
                print("Gracias por usar el programa. ¡Adiós!")
                break
            else:
                print("Opción no válida. Por favor, elige una opción del 1 al 3.")
        except ValueError:
            print("Error: Por favor, introduce un número válido.")


main()
