#==Generate By touchpy==

#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string
'''

def fake_bin(x:str):
    #binn = '0'.join([i for i in x if int(i) < 5]) + '1'.join([i for i in x if int(i) >= 1])

    #binn = ''

    #for i in x:
    #    if int(i) < 5:
    #        binn += '0'
    #    if int(i) >= 5:
    #        binn += '1'

    binn = ''.join(['0' if int(i) < 5 else '1' for i in x])
    return binn


if __name__ == "__main__":
    tests = [
            # [expected, input]
            ["01011110001100111", "45385593107843568"],
            ["101000111101101", "509321967506747"],
            ["011011110000101010000011011", "366058562030849490134388085"],
            ["01111100", "15889923"],
            ["100111001111", "800857237867"],
        ]
    
    try:
        for exp, inp in tests:
        # print(type(exp),type(int(inp)))
        print(fake_bin(inp))
        assert fake_bin(inp) == exp
    except AssertionError as e:
        print(e)
