#!/usr/bin/python3
# -*- coding: utf-8 -*-
# === Generate By Touchpy ===

'''
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
Examples

"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
'''

def order(sentence: str):

    list_sen = sentence.split()

    digit_dict = {word: int(''.join(filter(str.isdigit, word))) for word in list_sen if any(char.isdigit() for char in word)}
    
    sort_items_nums = sorted(digit_dict.items(), key=lambda x: x[1])
    
    return ' '.join(i[0] for i in sort_items_nums) 

if __name__ == "__main__":
    assert order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
    print(order("is2 Thi1s T4est 3a"))

