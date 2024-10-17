# Diccionario con los productos y sus precios unitarios
productos = {
    "Producto A": 10.50,
    "Producto B": 15.75,
    "Producto C": 7.20
}


# Función para ingresar las cantidades y calcular los subtotales
def ingresar_venta():
    venta = {}  # Almacena la cantidad y precio unitario por producto
    total = 0  # Total acumulado de la venta

    print("Ingrese las cantidades para cada producto:")

    for producto, precio in productos.items():
        while True:
            try:
                cantidad = int(input(f"{producto} (Precio unitario ${precio:.2f}): "))
                if cantidad < 0:
                    raise ValueError("La cantidad no puede ser negativa.")
                break
            except ValueError as e:
                print(f"Error: {e}. Intente nuevamente.")

        subtotal = cantidad * precio
        venta[producto] = {"cantidad": cantidad, "subtotal": subtotal}
        total += subtotal

    return venta, total


# Función para mostrar el resumen de la venta
def mostrar_resumen(venta, total):
    print("\nResumen de la venta:")
    for producto, datos in venta.items():
        print(f"{producto}: {datos['cantidad']} unidades -> Subtotal: ${datos['subtotal']:.2f}")
    print(f"\nTotal de la venta: ${total:.2f}")


# Función principal del programa
def realizar_venta():
    print("Bienvenido al sistema de ventas.")
    venta, total = ingresar_venta()
    mostrar_resumen(venta, total)


# Ejecutar el programa
if __name__ == "__main__":
    realizar_venta()
