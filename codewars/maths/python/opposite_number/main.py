#!/usr/bin/python3


def opposite(number):
    # your solution here
    if 0 == number:
        return 0

    if number >= 0:
        return -1 * number
    else:
        return abs(number)


if __name__ == "__main__":
    print(opposite(1))  # -1
    print(opposite(25.6))  # -25.6
    print(opposite(0))  # 0
    print(opposite(1425.2222))  # -1425.2222
    print(opposite(-3.1458))  # 3.1458
    print(opposite(-95858588225))  # 95858588225
