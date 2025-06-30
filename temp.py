from jellyfish import damerau_levenshtein_distance


def correct_typo(w1: str) -> str:
    wd1 = wd2 = ""
    for w2 in dictionary:
        d = damerau_levenshtein_distance(w1, w2)
        if d == 0:
            return f"{w1} 0"
        elif d == 1 and not wd1:
            wd1 = w2
        elif d == 2 and not wd2:
            wd2 = w2
    if wd1:
        return f"{w1} 1 {wd1}"
    if wd2:
        return f"{w1} 2 {find_intermediate_word(w1, wd2)} {wd2}"
    return f"{w1} 3+"


def find_intermediate_word(w1: str, w2: str) -> str | None:
    words = generate_intermediate_words(w1)
    for word in words:
        if damerau_levenshtein_distance(word, w2) == 1:
            return word


def generate_intermediate_words(w: str) -> set[str]:
    words = set()
    for i in range(len(w)):
        for j in range(ord("а"), ord("я") + 1):
            words.add(w[:i] + chr(j) + w[i + 1:])
    for i in range(len(w) + 1):
        for j in range(ord("а"), ord("я") + 1):
            words.add(w[:i] + chr(j) + w[i:])
    for i in range(len(w)):
        words.add(w[:i] + w[i + 1:])
    for i in range(len(w) - 1):
        words.add(w[:i] + w[i + 1] + w[i] + w[i + 2:])
    return words


with open("dict.txt", encoding="utf-8") as file_in:
    dictionary = file_in.read().splitlines()

with open("queries.txt", encoding="utf-8") as file_in:
    queries = file_in.read().splitlines()

corrections = []
for query in queries:
    corrections.append(correct_typo(query))

with open("corrections.txt", "w", encoding="utf-8") as file_out:
    file_out.write("\n".join(corrections))
