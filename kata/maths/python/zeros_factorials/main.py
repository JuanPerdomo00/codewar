#!/usr/bin/python3
# -*- coding: utf-8 -*-
# === Generate By Touchpy ===


from math import factorial
import re
import sys


"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html
Examples

zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros

Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.

"""



# MATCH = r"0+$"

# for n in range(1, 51):
#     if n % 5 != 0:
#         factorial_str = str(factorial(n))
#         match = re.search(MATCH, factorial_str)
#         if match:
#             last_zeros_count = len(match.group(0))
#             print(f"Factorial de {n}: {last_zeros_count} últimos ceros")
#         else:
#             print(f"No se encontraron ceros al final en el factorial de {n}!")
#             print(f"{factorial(n)}")
            
            

sys.set_int_max_str_digits(1000000)

def zeros(n):
    MATCH = re.search(r"0+$", str(factorial(n)))
    return len(MATCH.group(0)) if MATCH else 0

if __name__ == "__main__":
    # for x in range(1, 100):
    #     print(f"El factorial de {x}! tiene {zeros(x)} cantidad de ceros finales")
        
    
    print(zeros(0) == 0, "Testing with n = 0")
    
    print(zeros(6) == 1, "Testing with n = 6")
    
    print(zeros(30) == 7, "Testing with n = 30")
    
    print(zeros(100) == 24, "Testing with n = 100")
    
    print(zeros(1000) == 249, "Testing with n = 1000")
    
    print(zeros(100000) == 24999, "Testing with n = 100000")
    
    print(zeros(1000000000) == 249999998, "Testing with n = 1000000000")