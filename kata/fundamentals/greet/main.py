greetings: list[dict[str, str]] = [
    {"english": "Welcome"},
    {"czech": "Vitejte"},
    {"danish": "Velkomst"},
    {"dutch": "Welkom"},
    {"estonian": "Tere tulemast"},
    {"finnish": "Tervetuloa"},
    {"flemish": "Welgekomen"},
    {"french": "Bienvenue"},
    {"german": "Willkommen"},
    {"irish": "Failte"},
    {"italian": "Benvenuto"},
    {"latvian": "Gaidits"},
    {"lithuanian": "Laukiamas"},
    {"polish": "Witamy"},
    {"spanish": "Bienvenido"},
    {"swedish": "Valkommen"},
    {"welsh": "Croeso"},
]


def greet(language: str) -> str:
    return (
        "Welcome"
        if not [i for i in greetings if language in i]
        else [i[language] for i in greetings if language in i][0]
    )


print(greet("english"))
print(greet("dutch"))
print(greet("IP_ADDRESS_INVALID"))
print(greet(""))
print(greet("2"))
