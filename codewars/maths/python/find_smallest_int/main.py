#!/usr/bin/python3


"""
Given an array of integers your solution should find the smallest integer.

For example:
           Given [34, 15, 88, 2] your solution will return 2
           Given [34, -345, -1, 100] your solution will return -345

You can assume, for the purpose of this kata, that the supplied array will not be empty.
"""


def find_smallet_int(arr):
    return min(arr)


if __name__ == "__main__":
    print(find_smallet_int([33, 44, 22, 23, 45, 54, 66, 11]))  # 11
    print(find_smallet_int([2, 1, 3, 6, -1, -8, -9]))  # -1
