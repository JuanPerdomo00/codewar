#!/usr/bin/python3
# -*- coding: utf-8 -*-
# === Generate By Touchpy ===

"""
If the function is passed a valid PIN string, return true, else return false.
Examples (Input --> Output)

"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""

import re


def validate_pin(pin: str):
    return bool(re.fullmatch(r"^\d{4}(\d{2})?$", pin))


if __name__ == "__main__":
    print(
        "Should return False for pins which are not 4 or 6 digits long".center(30, "=")
    )
    print(validate_pin("1"), False, "Wrong output for '1'")
    print(validate_pin("12"), False, "Wrong output for '12'")
    print(validate_pin("123"), False, "Wrong output for '123'")
    print(validate_pin("12345"), False, "Wrong output for '12345'")
    print(validate_pin("1234567"), False, "Wrong output for '1234567'")
    print(validate_pin("-1234"), False, "Wrong output for '-1234'")
    print(validate_pin("-12345"), False, "Wrong output for '-12345'")
    print(validate_pin("1.234"), False, "Wrong output for '1.234'")
    print(validate_pin("00000000"), False, "Wrong output for '00000000'")

    print(
        "\nShould return False for pins which contain characters other than digits".center(
            30, "="
        )
    )
    print(validate_pin("a234"), False, "Wrong output for 'a234'")
    print(validate_pin(".234"), False, "Wrong output for '.234'")

    print("\nShould return True for valid pins".center(30, "="))
    print(validate_pin("1234"), True, "Wrong output for '1234'")
    print(validate_pin("0000"), True, "Wrong output for '0000'")
    print(validate_pin("1111"), True, "Wrong output for '1111'")
    print(validate_pin("123456"), True, "Wrong output for '123456'")
    print(validate_pin("098765"), True, "Wrong output for '098765'")
    print(validate_pin("000000"), True, "Wrong output for '000000'")
    print(validate_pin("123456"), True, "Wrong output for '123456'")
    print(validate_pin("090909"), True, "Wrong output for '090909'")
