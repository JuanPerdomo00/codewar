# ==Generate By touchpy==

#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Adenina -> Timina or Timina -> Adenina
Guanina -> Citosina or Citosina -> Guanina


"""


def DNA_strand(dna):
    base_nitrogenadas = {
        "A": "T",
        "T": "A",  # Adenina, Timina
        "G": "C",
        "C": "G",  # Guanina, Citosina
    }

    new_dna = ""

    for code in dna:
        for k, v in base_nitrogenadas.items():
            if code == k:
                new_dna += v

    return new_dna


if __name__ == "__main__":
    # Casos de prueba
    print(DNA_strand("AAAA"), "String AAAA is TTTT")
    print(DNA_strand("ATTGC"), "String ATTGC is ATTGC")
    print(DNA_strand("GTAT"), "String GTAT is GTAT")
