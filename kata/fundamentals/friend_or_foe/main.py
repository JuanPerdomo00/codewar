#!/usr/bin/python3
# -*- coding: utf-8 -*-
# === Generate By Touchpy ===


"""
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.

friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
"""


def friend(x):

    return list(filter(lambda y: len(y) == 4, x))


if __name__ == "__main__":
    print(
        friend(
            [
                "Ryan",
                "Kieran",
                "Mark",
            ]
        )
    )
    print(friend(["Ryan", "Jimmy", "abc", "d", "Cool Man"]))
    print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))
