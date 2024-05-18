import unittest
from svc.area_triangulo import calcular_area_triangulo


class TestCalcularAreaTriangulo(unittest.TestCase):

    def test_area_triangulo_valida(self):
        self.assertAlmostEqual(calcular_area_triangulo(3, 4, 5), 6.0)
        self.assertAlmostEqual(calcular_area_triangulo(7, 8, 9), 26.832815729997478)

    def test_lados_negativos_o_cero(self):
        with self.assertRaises(ValueError):
            calcular_area_triangulo(-1, 4, 5)
        with self.assertRaises(ValueError):
            calcular_area_triangulo(3, 0, 5)

    def test_lados_no_forman_triangulo(self):
        with self.assertRaises(ValueError):
            calcular_area_triangulo(1, 2, 3)
        with self.assertRaises(ValueError):
            calcular_area_triangulo(1, 10, 12)

    def test_lados_muy_pequenos(self):
        self.assertAlmostEqual(calcular_area_triangulo(0.1, 0.1, 0.1), 0.004330127018922194)


if __name__ == '__main__':
    unittest.main()