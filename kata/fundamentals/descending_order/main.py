# by: jakepys


def descending_order(num: int) -> int:
    return 0 if num <= 0 else int("".join(sorted(str(num)))[::-1])


def main():
    print(descending_order(0) == 0)  # 0
    print(descending_order(15) == 51)  # 51
    print(descending_order(123456789) == 987654321)  # 987654321
    # 987654321


if __name__ == "__main__":
    main()
