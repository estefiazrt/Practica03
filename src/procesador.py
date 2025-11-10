# src/procesador.py
import csv

class Analizador:
    # 1. REVISA BIEN: ESTE DEBE SER __init__ 
    def __init__(self, ruta_csv):
        self.ruta_csv = ruta_csv
        self.datos = self.leer_csv()

    def leer_csv(self):
        """
        Lee el archivo CSV usando el delimitador '|'
        y devuelve una lista de filas.
        """
        datos = []
        try:
            with open(self.ruta_csv, "r", encoding="utf-8") as archivo:
                #  2. CORRECCIÓN CLAVE: Usamos 'delimiter="|"' 
                lector = csv.DictReader(archivo, delimiter='|') 
                for fila in lector:
                    datos.append(fila)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.ruta_csv}.")
            return []
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo CSV: {e}")
            return []
            
        return datos

    def ventas_totales_por_provincia(self):
        """
        Devuelve un diccionario con el total de ventas por provincia.
        Usa las columnas 'PROVINCIA' y 'TOTAL_VENTAS'.
        """
        totales = {}
        
        for fila in self.datos:
            try:
                # Estandariza la provincia a mayúsculas
                provincia = fila["PROVINCIA"].strip().upper() 
                # Asegura que el valor se lea como flotante
                total_venta = float(fila["TOTAL_VENTAS"])

                # Suma al total existente o inicia en 0.0
                totales[provincia] = totales.get(provincia, 0.0) + total_venta

            except KeyError as e:
                # Esto atrapará errores si el encabezado del CSV no es el esperado
                print(f"Advertencia: El archivo CSV no tiene la columna {e}. Revise los encabezados.")
            except ValueError:
                print("Advertencia: Valor de venta inválido. Saltando fila.")

        return totales

    def ventas_por_provincia(self, nombre):
        """
        Devuelve el total de ventas de una provincia específica.
        """
        totales = self.ventas_totales_por_provincia()
        nombre_busqueda = nombre.strip().upper()

        return totales.get(nombre_busqueda, 0.0)