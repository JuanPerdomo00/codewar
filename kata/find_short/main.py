#!/usr/bin/python3
# -*- coding: utf-8 -*-
# === Generate By Touchpy ===

'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
'''

def find_short(s: str):
    #l = s.split(' ')
    #aux = 1
    #pdic = {}
    #print(l) # example ['bitcoin', 'take', 'over', 'the', 'world', 'maybe', 'who', 'knows', 'perhaps']
    #for i, palabra in enumerate(l):
        
    #if len(l[i]) > len(l[aux]) + 1 or len(l[i]) >= len(l[aux]):
       #     aux = len(l[i]) + 1
        
        #if len(l[i]) < len(l[aux - i]) or len(l[i]) <= len(l[aux - i]):
        #    pdic[i] = palabra
        #    aux = len(l[i]) + 1
        #else:
        #    print(pdic)

        return min(len(l) for l in s.split())
        

            


if __name__ == "__main__":
    print(find_short("bitcoin take over the world maybe who knows perhaps"))  # Output: 3
    print(find_short("turns out random test cases are easier than writing out basic ones"))  # Output: 3
    print(find_short("lets talk about javascript the best language"))  # Output: 3
    print(find_short("i want to travel the world writing code one day"))  # Output: 1
    print(find_short("Lets all go on holiday somewhere very cold"))  # Output: 2
    print(find_short("Let's travel abroad shall we"))  # Output: 2
