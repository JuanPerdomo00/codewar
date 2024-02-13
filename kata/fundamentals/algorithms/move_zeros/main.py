#!/usr/bin/python3
# -*- coding: utf-8 -*-
# === Generate By Touchpy ===


"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""

def move_zeros(lst):
    
    order = []
    
    if len(lst) == 0:
        return []
    
    for x in lst:
        if x <= 0:
            order.append(x)
     
    for y in lst:
        if y > 0:
            order.append(y)
    
    return sorted(order, key=lambda x: x == 0)

    

if __name__ == "__main__":
    move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) # [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]