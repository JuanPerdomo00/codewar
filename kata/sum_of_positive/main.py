#!/usr/bin/python3

'''
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
'''

def positive_sum(arr):
    add = 0
    for i in arr:
        if i <= 0:
            continue
        add += i

    return add if add > 0 else 0



if __name__ == "__main__":
    print(positive_sum([1, 2, 3, 4, 5]), "== 15")
    print(positive_sum([1, -2, 3, 4, 5]), "== 13")
    print(positive_sum([-1, 2, 3, 4, -5]), "== 9")
    print(positive_sum([]), "== 0")
    print(positive_sum([-1, -2, -3, -4, -5]), "== 0")
