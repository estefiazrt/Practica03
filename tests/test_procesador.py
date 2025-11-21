import unittest
from src.procesador import Analizador


class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #  RUTA para que sea igual en app.py
        cls.analizador = Analizador("datos/sri_ventas_2024.csv")
        cls.resumen = cls.analizador.ventas_totales_por_provincia()

    def test_numero_provincias_coherente(self):
        # al menos 10 provincias, puedes subir el número
        self.assertGreaterEqual(len(self.resumen), 10)

    def test_valores_numericos_y_no_negativos(self):
        for total in self.resumen.values():
            self.assertIsInstance(total, (int, float))
            self.assertGreaterEqual(total, 0)

    def test_provincia_existente(self):
        # cambiar o añadir otras provincias 
        self.assertIn("PICHINCHA", self.resumen)

    def test_ventas_por_provincia_consistente(self):
        total_dic = self.resumen["PICHINCHA"]
        total_func = self.analizador.ventas_por_provincia("PICHINCHA")
        # comparamos con 2 decimales 
        self.assertAlmostEqual(total_dic, total_func, places=2)


if __name__ == "__main__":
    unittest.main()
