#!/usr/bin/python3
# -*- coding: utf-8 -*-
# === Generate By Touchpy ===


"""
a = 011 -> 3
b = 010 -> 2
################################################################################################################################
 Xor Bit a Bit
 011
 010
-------
 001 -> 1
################################################################################################################################
 And Bit a Bit
 011
 010
------
 010 -> 2
################################################################################################################################
 Or bit a bit
 011
 010
------
 011 -> 2
################################################################################################################################
 Not bit a bit
 Cuando se opera con not se da lo contrario en signo mas -1
 ~011 = -011+(-1) = -100 = -4
 ~010 = -010+(-1) = -011 = -3

 Lo contrario pasaria si el binario fuera desde un principio negativo
 ~-011 Seria 2, porque cambia designo a positivo y ademas le resta 1 por lo que quedaria asi.
 -3 + 1, dinde -3 es la entrada que hacemos para operar.
 ~-3 = 2 ~-011 = +010
################################################################################################################################
 Dasplazamiento a la derecha n bit
 a >> 1 # Con esto se le dice que desplaze un bit a la derecha

 011 >> 1 = 32 16 8 4 2 1
                    0 1 1
                      0 1 [1]-> Este bit queda fuera del rango, por ende quedara convertido en 01 o 1

    Ahora desplazemolo 2 bit a la derecha, que pasaria?
    32 16 8 4 2 1
            0 1 1
                0 [1 1] -> 2 bits quedan fuera del rangom convirtiendo en 0 o 0 entero.
################################################################################################################################

 Desplazamiento a la izquierda n bit
 a << 1 # Con esto se le dice que se desplaze un bit a la izquerda

 011 << 1 = 32 16 8 4 2 1
                    0 1 1
                    1 1 0 -> Se desplazo un bit a la izquierda, quedando asi en 110 o 6 entero.

      Ahora desplazemolo 2 bits a la izquierda, que pasaria?
      32 16 8 4 2 1
              0 1 1
          0 1 1 0 0     -> Se desplazo 2 bits a la izquierda, quedando asi en 01100 o 12 entero.


Apuntes by Jakepys.
"""

"""
    Task

Given Two integers a , b , find The sum of them , BUT You are not allowed to use the operators + and -
Notes

    The numbers (a,b) may be positive , negative values or zeros .

    Returning value will be an integer .

    Julia: +, -, sum, cumsum, diff, run, muladd, fma, count, Symbol and Expr are disabled.

Input >> Output Examples

1- Add (5,19) ==> return (24) 

2- Add (-27,18) ==> return (-9)

3- Add (-14,-16) ==> return (-30)


"""


def add(a, b):
    while b != 0:
        com = a & b
        a ^= b
        b = com << 1
    return a


if __name__ == "__main__":
    print(add(2, 3))
