from typing import List


def sum_two_smallest_numbers(numbers: List[int]) -> int:
    ordened_ln = sorted(numbers)
    return ordened_ln[0] + ordened_ln[1]


def main():
    print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
    print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))
    print(sum_two_smallest_numbers([25, 42, 12, 18, 22]))


if __name__ == "__main__":
    main()
