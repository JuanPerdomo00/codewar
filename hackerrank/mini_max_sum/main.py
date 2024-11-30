#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

from typing import List


def mini_max_sum(arr: List[int]) -> int:
    # Write your code here
    return (
        f"{sum(arr[:-1])} {sum(arr[:-1])}"
        if len(set(arr)) == 1
        else f"{sum([i for i in arr if i < max(arr)])} {sum([i for i in arr if i > min(arr)])}"
    )


# sum([i for i in arr if i < max(arr)]), sum([i for i in arr if i > min(arr)])


if __name__ == "__main__":
    print(mini_max_sum([1, 3, 5, 7, 9]))
    print(mini_max_sum([1, 2, 3, 4, 5]))
    print(mini_max_sum([5, 5, 5, 5, 5]))
