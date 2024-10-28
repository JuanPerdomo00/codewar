# ==Generate By touchpy==

#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
"""


def bmi(weight, height):
    op = weight / height**2

    if op <= 18.5:
        return "Underweight"
    elif op <= 25.0:
        return "Normal"
    elif op <= 30.0:
        return "Overweight"
    elif op > 30:
        return "Obese"


if __name__ == "__main__":
    print(bmi(50, 1.80))
    print(bmi(80, 1.80))
    print(bmi(90, 1.80))
    print(bmi(110, 1.80))
    print(bmi(50, 1.50))
