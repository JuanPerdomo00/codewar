#!/usr/bin/python3
# -*- coding: utf-8 -*-
# === Generate By Touchpy ===


def row_sum_odd_numbers(n):
    # Inicializamos una lista para almacenar la pirámide de números impares
    pyramid_list = []

    # Inicializamos un contador para los números impares
    odd_num = 1

    # Bucle para generar las filas de la pirámide
    for i in range(n):
        # Inicializamos una lista para la fila actual
        row_list = []
        # Añadimos números impares a la fila actual
        for j in range(i + 1):
            row_list.append(odd_num)
            odd_num += 2
        # Añadimos la fila actual a la pirámide
        pyramid_list.append(row_list)

    return sum(pyramid_list[-1])


if __name__ == "__main__":
    print(row_sum_odd_numbers(5) == 125)
    print(row_sum_odd_numbers(1) == 1)
    print(row_sum_odd_numbers(2) == 8)
    print(row_sum_odd_numbers(13) == 2197)
    print(row_sum_odd_numbers(19) == 6859)
    print(row_sum_odd_numbers(41) == 68921)
