def reverse_words(text: str):
    #go for it
    return ' '.join(i[::-1] for i in text.split(" "))


if __name__ == "__main__":
    reverse_words('The quick brown fox jumps over the lazy dog.')
    reverse_words('apple')
    reverse_words('a b c d')
    reverse_words('  double  spaced  words  ')