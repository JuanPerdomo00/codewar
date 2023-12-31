#!/usr/bin/python3
# -*- coding: utf-8 -*-
# === Generate By Touchpy ===

'''
Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 --> [5,4,3,2,1]
'''

def reverse_seq(n):
    r = [i for i in range(1, n + 1)]
    r.reverse()
    return r

if __name__ == "__main__":
    print(reverse_seq(5), '[5, 4, 3, 2, 1]')
    print(reverse_seq(10), '[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]')


