#!/usr/bin/python3
# -*- coding: utf-8 -*-
# === Generate By Touchpy ===



'''
For this exercise you will create a global flatten method. The method takes in any number of arguments and flattens them into a single array.
If any of the arguments passed in are an array then the individual objects within the array will be flattened so that they exist at the same level as the other arguments.
Any nested arrays, no matter how deep, should be flattened into the single array result.

The following are examples of how this function would be used and what the expected results would be:

flatten(1, [2, 3], 4, 5, [6, [7]]) # returns [1, 2, 3, 4, 5, 6, 7]
flatten('a', ['b', 2], 3, None, [[4], ['c']]) # returns ['a', 'b', 2, 3, None, 4, 'c']
'''






def flatten(*args):
    list_new = []
    arr_args = list(args)
    
    for x in arr_args:
        if isinstance(x, list):
            list_new.extend(flatten(*x))
        else:
            list_new.append(x)

    return list_new


if __name__ == "__main__":
    print(1, flatten(1, [2, 3], 4, 5, [6, [7]]))
    print(2, flatten('a', ['b', 2], 3, None, [[4], ['c']]))
    print(3, flatten()) #[]
    print(4, flatten(1, 2, 3)) # [1, 2, 3])
    print(5, flatten([1, 2], [3, 4, 5], [6, [7], [[8]]])) # [1, 2, 3, 4, 5, 6, 7, 8])
    print(6, flatten(1, 2, ['9', [], []], None)) # [1, 2, '9', None])
    print(7, flatten(['hello', 2, ['text', [4, 5]]], [[]], '[list]')) # ['hello', 2, 'text', 4, 5, '[list]'])

