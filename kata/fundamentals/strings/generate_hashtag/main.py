# By: Jakepys

def generate_hashtag(s: str) -> str:
    # your code here
    s = s.strip()
    return (
        False
        if len(s) == 0
        else f"#{s.capitalize()}"
        if len(s.split()) == 1
        else False
        if len(f"#{''.join(i.capitalize() for i in s.split())}") > 140
        else f"#{''.join(i.capitalize() for i in s.split())}"
    )


if __name__ == "__main__":
    print(generate_hashtag("Codewars"))  # Codewars
    print(generate_hashtag("Codewars      "))  # Codewars
    print(generate_hashtag("      Codewars"))  # Codewars
    print(generate_hashtag("Codewars Is Nice"))
    print(generate_hashtag("codewars is nice"))
    print(generate_hashtag("CoDeWaRs is niCe"))
    print(generate_hashtag("c i n"))
    print(generate_hashtag("codewars  is  nice"))
    print(generate_hashtag(""))
    print(
        generate_hashtag(
            "Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat"
        )
    )
