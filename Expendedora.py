print("""Escriba el código del producto que desee comprar:
AA11 - Soda ($20)
BB22 - Galleta ($10)
CC33 - Papitas ($15)
Escriba 'salir' para finalizar la compra.
""")

# Diccionario de productos con su inventario y precio
productos = {
    "Soda": {"precio": 20, "inventario": 5},
    "Galleta": {"precio": 10, "inventario": 5},
    "Papitas": {"precio": 15, "inventario": 5}
}

# Función para procesar el código del producto
def procesar_codigo(codigo):
    if codigo == "AA11":
        producto = "Soda"
    elif codigo == "BB22":
        producto = "Galleta"
    elif codigo == "CC33":
        producto = "Papitas"
    else:
        print("Código inválido. Intente de nuevo.")
        return

    # Verificar si hay inventario
    if productos[producto]["inventario"] > 0:
        productos[producto]["inventario"] -= 1
        print(f"Has comprado una {producto}. Precio: ${productos[producto]['precio']}.")
    else:
        print(f"Lo siento, {producto} está agotado.")

# Bucle principal para permitir compras múltiples
while True:
    codigo = input("> ")
    if codigo.lower() == "salir":
        print("Gracias por su compra. ¡Hasta luego!")
        break
    procesar_codigo(codigo)

# Mostrar inventario restante
print("\nInventario final:")
for producto, detalles in productos.items():
    print(f"{producto}: {detalles['inventario']} unidades restantes.")
