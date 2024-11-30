#!/usr/bin/python3

"""
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.
"""


def find_average(numbers):
    # your code here
    return 0 if 0 == len(numbers) else sum(numbers) / len(numbers)


if __name__ == "__main__":
    print(find_average([1, 2, 3, 4, 5]))
    print(find_average([1, 2, 3]))  #  2
    print(find_average([]))  # 0
    print(find_average([1, 2]))  # 1.5
