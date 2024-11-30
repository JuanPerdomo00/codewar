# ==Generate By touchpy==

#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
En todo triángulo la suma de las longitudes de dos lados cualesquiera es siempre mayor a la longitud del lado restante.

|a+b| > |c|, |a+c| > |b| y |b+c| > |a|.
"""


def is_triangle(a, b, c):
    return True if abs((a + b) > c) and abs((a + c) > b) and abs((b + c) > a) else False


if __name__ == "__main__":
    # Casos de prueba
    print(is_triangle(1, 2, 2), "didn't work when sides were 1, 2, 2")
    print(is_triangle(7, 2, 2), "didn't work when sides were 7, 2, 2")
    print(is_triangle(1, 2, 3), "didn't work when sides were 1, 2, 3")
    print(is_triangle(1, 3, 2), "didn't work when sides were 1, 3, 2")
    print(is_triangle(3, 1, 2), "didn't work when sides were 3, 1, 2")
    print(is_triangle(5, 1, 2), "didn't work when sides were 5, 1, 2")
    print(is_triangle(1, 2, 5), "didn't work when sides were 1, 2, 5")
    print(is_triangle(2, 5, 1), "didn't work when sides were 2, 5, 1")
    print(is_triangle(4, 2, 3), "didn't work when sides were 4, 2, 3")
    print(is_triangle(5, 1, 5), "didn't work when sides were 5, 1, 5")
    print(is_triangle(2, 2, 2), "didn't work when sides were 2, 2, 2")
    print(is_triangle(-1, 2, 3), "didn't work when sides were -1, 2, 3")
    print(is_triangle(1, -2, 3), "didn't work when sides were 1, -2, 3")
    print(is_triangle(1, 2, -3), "didn't work when sides were 1, 2, -3")
    print(is_triangle(0, 2, 3), "didn't work when sides were 0, 2, 3")
