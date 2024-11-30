def to_jade_case(s: str) -> str:
    return s.title()


if __name__ == "__main__":
    print(
        to_jade_case(
            "All the rules in this world were made by someone no smarter than you. So make your own."
        )
        == "All The Rules In This World Were Made By Someone No Smarter Than You. So Make Your Own."
    )
