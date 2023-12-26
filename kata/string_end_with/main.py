# ==Generate By touchpy==

#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution'(abc', 'd') # returns false
'''


def end_with(text, end):
    return True if text[-len(end):] == end else False


if __name__ == "__main__":
    fixed_tests_True = (
        ("samurai", "ai"),
        ("ninja",   "ja"),
        ("sensei",  "i"),
        ("abc",     "abc"),
        ("abcabc",  "bc"),
        ("fails",   "ails"),
    )

    fixed_tests_False = (
        ("sumo",    "omo"),
        ("samurai", "ra"),
        ("abc",     "abcd"),
        ("ails",    "fails"),
        ("this",    "fails"),
        ("spam",    "eggs")
    )

    for text, end in fixed_tests_True:
        print(end_with(text, end))
    
    for text, end in fixed_tests_False:
        print(end_with(text, end))

