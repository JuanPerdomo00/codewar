#==Generate By touchpy==

#!/usr/bin/python3
# -*- coding: utf-8 -*-


def find_needle(haystack):
    for position, types in enumerate(haystack):
        if isinstance(types, str) and types == 'needle':
            return f'found the needle at position {position}'
  
    


if __name__ == "__main__":
   print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))
