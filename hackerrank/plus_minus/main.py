from typing import List
import random


def plus_minus(arr: List[int]):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0

    for i in arr:
        if i <= 0:
            if i == 0:
                zero += 1
            else:
                neg += 1
        else:
            pos += 1
    else:
        # print(f"zero: {zero} pos: {pos} neg: {neg}")
        pos /= len(arr)
        zero /= len(arr)
        neg /= len(arr)
    return "\n".join(f"{i:.8f}" for i in [pos, neg, zero])


if __name__ == "__main__":
    print(plus_minus([-4, 3, -9, 0, 4, 1]))
    print(plus_minus([random.randint(-10, 10) for _ in range(50000)]))
