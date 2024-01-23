#!/usr/bin/python3
# -*- coding: utf-8 -*-
# === Generate By Touchpy ===


import unittest


def wave(string: str) -> list:
    resultado: list = []
    for a in range(len(string)):
        if string[a].isalpha():
            resultado.append(f"{string[:a]}{string[a].upper()}{string[a+1:]}")
        continue

    
    return resultado




class TestWaveFunction(unittest.TestCase):

    def test_wave_example1(self):
        result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
        self.assertEqual(wave("hello"), result)

    def test_wave_example2(self):
        result = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
        self.assertEqual(wave("codewars"), result)

    def test_wave_example3(self):
        result = []
        self.assertEqual(wave(""), result)

    def test_wave_example4(self):
        result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
        self.assertEqual(wave("two words"), result)

    def test_wave_example5(self):
        result = [" Gap ", " gAp ", " gaP "]
        self.assertEqual(wave(" gap "), result)

    def test_wave_example6(self):
        result = ["A       b    ", "a       B    "]
        self.assertEqual(wave("a       b    "), result)

    def test_wave_example7(self):
        result = ["This is a few words", "tHis is a few words", "thIs is a few words", "thiS is a few words", "this Is a few words", "this iS a few words", "this is A few words", "this is a Few words", "this is a fEw words", "this is a feW words", "this is a few Words", "this is a few wOrds", "this is a few woRds", "this is a few worDs", "this is a few wordS"]
        self.assertEqual(wave("this is a few words"), result)

if __name__ == '__main__':
    unittest.main()