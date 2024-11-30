#!/usr/bin/python3
# -*- coding: utf-8 -*-
# === Generate By Touchpy ===

"""
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
Examples

    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""


# Error objects modified
# class Root_Digits:
#    def __init__(self, n: int):
#        self.n = n
#        self.__nodes = {}
#        self.__branch = 0
#
#    def watch(self):
#        aux_dict = {}
#        arrn = [int(i) for i in str(self.n) if i != "1"]
#        aux_dict[f"Root: {arrn}"] = sum(arrn)
#
#        for value in self.__nodes.values():
#            if len(str(value)) > 1:
#                arrn = [int(i) for i in str(value) if i != '1']
#                self.__branch += 1
#                new_key = f"branch {self.__branch} == {arrn}"
#                aux_dict[new_key] = sum(arrn)
#
#        self.__nodes = aux_dict

#        return self.__nodes


def digital_root(n: int) -> int:
    strn: str = str(n)
    sumn: int = 0

    for x in strn:
        sumn += int(x)

    return digital_root(sumn) if sumn >= 10 else sumn


if __name__ == "__main__":
    print(digital_root(16) == 7)
    print(digital_root(942) == 6)
    print(digital_root(132189) == 6)
    print(digital_root(493193) == 2)
