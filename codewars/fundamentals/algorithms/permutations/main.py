import itertools


def permutations(s):
    # Code Away!
    return ["".join(p) for p in set(itertools.permutations(s))]


print(permutations("a"))
print(permutations("ab"))
print(permutations("aabb"))
