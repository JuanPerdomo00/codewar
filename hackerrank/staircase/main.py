import time
#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#


def staircase(n):
    """Example

        `n = 4`

       #\n
      ##\n
     ###\n
    ####\n

        Args:
            n (int): number
    """
    # Write your code here
    spaces = [i - 1 for i in range(1, n + 1)][::-1]
    # print(spaces)
    for i in range(0, n):
        # print(spaces[0:len(spaces)])
        # Ok originally it is with a # but I changed it for a snake emoji I love python haha
        print(spaces[i] * " " + "🐍" * (i + 1))


if __name__ == "__main__":
    # staircase(4)
    # staircase(6)

    for i in range(1, 26):
        staircase(i)
        time.sleep(1)


#     #
#     #
