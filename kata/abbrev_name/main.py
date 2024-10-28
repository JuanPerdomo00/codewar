# ==Generate By touchpy==

#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

    Sam Harris => S.H

    patrick feeney => P.F
"""


def abbrev_name(name: str):
    l = list(map(lambda n: n.capitalize()[0], name.split(" ")))
    return f"{l[0]}.{l[1]}"


if __name__ == "__main__":
    print(abbrev_name("juan perdomo"))
