def create_phone_number(n):
    import re;return re.sub(r"(\d{3})(\d{3})(\d{4})", r"(\1) \2-\3", "".join(str(i) for i in n))


if __name__ == "__main__":
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
