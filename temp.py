from jellyfish import damerau_levenshtein_distance


def find_match(s1: str) -> str:
    s1 = normalize_university_name(s1)
    result = ""
    mnd = 1000
    for s2 in universities_normalized.keys():
        d = damerau_levenshtein_distance(s1, s2)
        if mnd > d:
            mnd = d
            result = s2
    return universities_normalized[result]


def normalize_university_name(name: str) -> str:
    return name.lower().translate(str.maketrans('', '', '(),«»"-–—'))


with open("universities.txt", encoding="utf-8") as file_in:
    universities = file_in.read().splitlines()

universities_normalized = {
    normalize_university_name(name): name for name in universities
}

with open("queries.txt", encoding="utf-8") as file_in:
    queries = file_in.read().splitlines()

matches = []
for query in queries:
    matches.append(find_match(query))
    print(len(matches))

with open("matches.txt", "w", encoding="utf-8") as file_out:
    file_out.write("\n".join(matches))
