def counter(text):
    d = dict()
    for c in text:
        if c.isalpha():
            d[c] = d.get(c, 0) + 1
    for c, k in sorted(d.items()):
        yield c, k


if __name__ == '__main__':
    text = "The quick brown fox jumps over a lazy dog."
    for letter, count in counter(text):
        print(letter, count, sep="-", end=", ")
