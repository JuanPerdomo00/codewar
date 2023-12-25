#==Generate By touchpy==

#!/usr/bin/python3
# -*- coding: utf-8 -*-

def filter_list(arr):
    return list(filter(lambda x: isinstance(x, int), arr))


if __name__ == "__main__":
    print(filter_list([1, 2, 'a', 'b']))
    print(filter_list([1, 'a', 'b', 0, 15]))
    print(filter_list([1, 2, 'aasf', '1', '123', 123]))
