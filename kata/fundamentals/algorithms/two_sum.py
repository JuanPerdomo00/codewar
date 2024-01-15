#!/usr/bin/python3
# -*- coding: utf-8 -*-
# === Generate By Touchpy ===

"""
Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

Based on: https://leetcode.com/problems/two-sum/

two_sum([1, 2, 3], 4) # returns (0, 2) or (2, 0)
two_sum([3, 2, 4], 6) # returns (1, 2) or (2, 1)
"""


def two_sum(n, t):
    tuple_position = []

    for x, num_x in enumerate(n):
        for y, num_y in enumerate(n):
            if x != y and num_x + num_y == t:
                tuple_position.append((x, y))
            else:
                continue

    return tuple_position[0] or tuple_position[1]


if __name__ == "__main__":
    sample_test_cases = [
        #   numbers      target      valid results
        ([1, 2, 3], 4, ((0, 2), (2, 0))),
        ([1234, 5678, 9012], 14690, ((1, 2), (2, 1))),
        ([2, 2, 3], 4, ((0, 1), (1, 0))),
    ]

    for numbers, target, valid_result in sample_test_cases:
        print(two_sum(numbers, target))

