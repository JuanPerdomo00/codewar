#!/usr/bin/python3
# -*- coding: utf-8 -*-
# === Generate By Touchpy ===


"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

    []                                -->  "no one likes this"
    [Peter""]                         -->  "Peter likes this"
    ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
    ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
    ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

    Note: For 4 or more names, the number in "and 2 others" simply increases.]
"""


def like(names: list) -> str:
    return (
        "no one likes this"
        if len(names) == 0
        else (
            f"{names[0]} likes this"
            if len(names) == 1
            else (
                f"{names[0]} and {names[1]} like this"
                if len(names) == 2
                else (
                    f"{names[0]}, {names[1]} and {names[2]} like this"
                    if len(names) == 3
                    else (
                        f"{names[0]}, {names[1]} and {len(names[2:])} others like this"
                        if len(names) >= 4
                        else ""
                    )
                )
            )
        )
    )


if __name__ == "__main__":
    print(like([]))
    print(like(["Peter"]))
    print(like(["Jacob", "Alex"]))
    print(like(["Max", "John", "Mark"]))
    print(like(["Max", "John", "Mark", "Mark"]))
    print(like(["Max", "John", "Mark", "Marak", "Jakepys"]))
    try:
        assert like([]) == "no one likes this"
        assert like(["Peter"]) == "Peter likes this"
        assert like(["Jacob", "Alex"]) == "Jacob and Alex like this"
        assert like(["Max", "John", "Mark"]) == "Max, John and Mark like this"
        assert (
            like(["Alex", "Jacob", "Mark", "Marak"])
            == "Alex, Jacob and 2 others like this"
        )
    except AssertionError as e:
        print(e)
