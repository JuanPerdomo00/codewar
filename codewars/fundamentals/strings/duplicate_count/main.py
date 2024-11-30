def duplicate_count(text: str) -> int:
    from collections import Counter

    # Your code goes here
    lter = Counter([i for i in text.lower() if i.isalpha()])
    digit = Counter([i for i in text.lower() if i.isnumeric()])

    repear = 0

    for _, count in lter.items():
        if count > 1:
            repear += 1

    for _, count in digit.items():
        if count > 1:
            repear += 1
    return repear


print(duplicate_count(""))  # 0
print(duplicate_count("abcde"))  # 0
print(duplicate_count("abcdeaa"))  # 1
print(duplicate_count("abcdeaB"))  # 2
print(duplicate_count("Indivisibilities"))  # 2
