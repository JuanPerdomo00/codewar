#==Generate By touchpy==

#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
If you can't sleep, just count sheep!!
Task:

    Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.
'''


def count_sheep(n):
    return ''.join([f'{i} sheep...' for i in range(1, n + 1)])


if __name__ == "__main__":
    print(count_sheep(1))
    print(count_sheep(2))
    print(count_sheep(3))
    print(count_sheep(4))
    print(count_sheep(5))
    print(count_sheep(6))
    print(count_sheep(7))
    print(count_sheep(8))
    print(count_sheep(9))
    print(count_sheep(10))
