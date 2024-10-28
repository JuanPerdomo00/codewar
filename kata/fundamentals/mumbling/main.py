#!/usr/bin/python3
# -*- coding: utf-8 -*-
# === Generate By Touchpy ===

"""
This time no story, no theory. The examples below show you how to write function accum:
    Examples:

    accum("abcd" ->) A-Bb-Ccc-Dddd""
    accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    accum"(cwAt") -> "C-Ww-Aaa-Tttt"

    The parameter of accum is a string which includes only letters from a..z and A..Z.
"""


def accum(s: str):
    ss = ""
    for i, char in enumerate(s):
        ss += char.capitalize() + char.lower() * i + "-"

    return ss[:-1]


if __name__ == "__main__":
    print(accum("ZpglnRxqenU"))
