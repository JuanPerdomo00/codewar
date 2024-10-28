#!/usr/bin/python3
# -*- coding: utf-8 -*-
# === Generate By Touchpy ===


"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

    unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
    unique_in_order'(ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
    unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
    unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
"""


def unique_in_order(s: str) -> list[str]:
    exists = []

    for item in s:
        if not exists or item != exists[-1]:
            exists.append(item)

    return exists


if __name__ == "__main__":

    print(unique_in_order("ABBCcA"))
    print(unique_in_order("AAAABBBCCDAABBB"))
    print(unique_in_order([1, 2, 2, 3, 3]))

    print("Should work with empty sequence")
    print(unique_in_order("") == [])
    print(unique_in_order([]) == [])
    print(unique_in_order(()) == [])

    print("Should work with single element sequence")
    print(unique_in_order("A") == ["A"])
    print(unique_in_order(["A"]) == ["A"])
    print(unique_in_order(("A",)) == ["A"])

    print("Should reduce duplicates")
    print(unique_in_order("AA") == ["A"])
    print(unique_in_order("AAAABBBCCDAABBB") == ["A", "B", "C", "D", "A", "B"])

    print("Should be case-sensitive")
    print(unique_in_order("ABBCcA") == ["A", "B", "C", "c", "A"])

    print("Should work with different element types")
    print(unique_in_order([1, 2, 3, 3, -1]) == [1, 2, 3, -1])
    print(unique_in_order(["a", "b", "b", "a"]) == ["a", "b", "a"])
