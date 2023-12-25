#!/usr/bin/python3

def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    i = 0
    aux = 0
    ls = []
    while i < n:
        aux += x
        ls.append(aux)
        i += 1


    return ls





        

            





if __name__ == "__main__":
    print(count_by(1,5))
    print(count_by(2,5))
    print(count_by(3,5))
    print(count_by(50,5))
    print(count_by(100,5))

