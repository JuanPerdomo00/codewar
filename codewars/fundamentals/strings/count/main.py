def conut(s: str):
    # return {} if len(s) == 0 else [(i, x) for i, x in enumerate(s)]
    if not len(s):
        return {}

    new_dict = {}
    for char in s:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1

    return new_dict


"""
I really didn't know that, it didn't occur to me :*
"""


def test(s: str):
    from collections import Counter

    return Counter(s)


if __name__ == "__main__":
    # print(conut(""))
    # print(conut("abae"))
    # print(conut("aba"))
    # print(conut("aabb"))

    print(test("abaeeaa"))
