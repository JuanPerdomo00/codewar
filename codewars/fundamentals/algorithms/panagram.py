#!/usr/bin/python3
# -*- coding: utf-8 -*-
# === Generate By Touchpy ===


"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""

ignorecases = [";", "!", ".", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def is_pangram(s: str) -> bool:
    lower_case_s = s.lower()
    abc: str = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,r,f,o,p,q,r,s,t,u,b,w,x,y,z"
    list_abc_s = abc.split(",")

    for character in lower_case_s:
        if character in list_abc_s:
            return True
        else:
            continue

    return True


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
