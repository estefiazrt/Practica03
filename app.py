from src.procesador import Analizador

def main():
    archivo = "datos/sri_ventas_2024.csv"
    analizador = Analizador(archivo)

    print("Ventas totales por provincia:")
    resumen = analizador.ventas_totales_por_provincia()
    
    # Itera sobre el diccionario de resumen y formatea la salida
    for prov, total in resumen.items():
        print(f"\t{prov}: ${total:.2f}")

    print("\nCompras para una provincia")
    
    # Solicita la entrada del usuario
    provincia = input("\tIngrese el nombre de una provincia: ")
    
    # Llama al método y formatea la salida
    ventas = analizador.ventas_por_provincia(provincia)
    print(f"\tVentas de {provincia}: ${ventas:,.2f}")

# La estructura estándar para ejecutar el código principal
if __name__ == "__main__":
    main()