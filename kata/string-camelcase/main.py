#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""

import re


def to_camel_case(text: list[str]) -> str:
    list_strigs = [t for t in text]
    print(list_strigs)
    words = re.split(r'[-_]', [tex for tex in text])
    finally_words = ''
    for word in words:
        finally_words += ''.join(word.capitalize())

    return finally_words
    #return words[0] + ''.join(words.capitalize() for word in words[1:])


def main() -> None:
    list_strigs: list[str] =  ["the-stealth-warrior", "The_Stealth_Warrior", "The_Stealth-Warrior"]
    string: str = to_camel_case(list_strigs)
    print(string)


if __name__ == "__main__":
    main()
