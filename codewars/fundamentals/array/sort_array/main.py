# You will be given an array of numbers.
# You have to sort the odd numbers
#  in ascending order while leaving the even numbers at their original positions.

# By: Jakepys

from typing import List


def is_ord(n: int) -> bool:
    return True if n % 2 == 0 else False


def is_odd(n: int) -> bool:
    return True if n % 2 != 0 else False


def sort_array(source_array: List[int]) -> List[int]:
    if len(source_array) == 0:
        return []

    new_list = []

    for i, num in enumerate(source_array):
        if is_odd(num):
            if len(new_list) == 0:
                new_list.append(num)
            else:
                new_list.insert(i - 2, num)

    return new_list


def main():
    print(sort_array([5, 3, 2, 8, 1, 4, 11]))  # [1, 3, 2, 8, 5, 4, 11]


if __name__ == "__main__":
    main()
