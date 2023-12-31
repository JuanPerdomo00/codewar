#!/usr/bin/python3
# -*- coding: utf-8 -*-
# === Generate By Touchpy ===



'''
Let's define two functions:

    S(N) — sum of all positive numbers not more than N
    S(N) = 1 + 2 + 3 + ... + N

    Z(N) — sum of all S(i), where 1 <= i <= N
    Z(N) = S(1) + S(2) + S(3) + ... + S(N)

    You will be given an integer N as input; your task is to return the value of S(Z(N)).

    For example, let N = 3:

        Z(3) = 1 + 3 + 6 = 10
        S(Z(3)) = S(10) = 55

        The input range is 1 <= N <= 10^9 and there are 80 ( 40 in LC ) test cases, of which most are random.
'''


#def sum_of_sums(n):
#    z = lambda n: sum(((x * n) - (x + 1)) for x in range(1, n + 1)) + 1
#
#    def s(z):
#        num = z(n)
#        return sum(range(1, num + 1))

#    return s(z)


def sum_of_sums(N):
    # EL enfoque era mas matematico que usar una funcion que iterba.
    def S(N):
        return (N * (N + 1)) // 2

    def Z(N):
        return N * (N+1) * (N+2) // 6

    return S(Z(N))


if __name__ == "__main__":
    print(f"Input {sum_of_sums(3)} ", "to return 55")
    print(f"Input {sum_of_sums(5)} ", "to return 630")
    print(f"Input {sum_of_sums(100)} ", "to return 14740530850")
