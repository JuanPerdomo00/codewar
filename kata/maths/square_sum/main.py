#==Generate By touchpy==

#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 12+22+22=91^2 + 2^2 + 2^2 = 912+22+22=9.
'''


def square_sum(numbers):
    return sum(abs(i ** 2) for i in numbers) if len(numbers) > 0 else 0

if __name__ == "__main__":
    print(square_sum([1, 2]))
    print(square_sum([0, 3, 4, 5]))
    print(square_sum([]))
    print(square_sum([-1, -2]))
    print(square_sum([-1, 0, 1]))
