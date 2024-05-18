import math


def calcular_area_triangulo(a, b, c):
    """
    Calcula el área de un triángulo dados sus tres lados usando la fórmula de Herón.

    :param a: Lado a del triángulo.
    :param b: Lado b del triángulo.
    :param c: Lado c del triángulo.
    :return: Área del triángulo.
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Los lados deben ser mayores que cero.")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("La suma de dos lados debe ser mayor que el tercer lado.")

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area