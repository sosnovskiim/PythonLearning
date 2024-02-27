"""
В файле "text.txt" задан текст, состоящий из предложений, разделённых знаками препинания из набора «.?!».
Предложения в свою очередь состоят из слов, отделённых друг от друга пробелами.
Найти слова (без учёта регистра) и их количество, которые
встречаются одновременно и в повествовательных, и в восклицательных предложениях,
но не встречаются в вопросительных.
"""
with open('text.txt', encoding='utf-8') as f:
    s = f.read().split()
narrative_set, exclamatory_set, interrogative_set = set(), set(), set()
temp = set()
for w in s:
    if w[-1] == '.':
        temp.add(w[:-1].lower())
        narrative_set |= temp
        temp.clear()
    elif w[-1] == '!':
        temp.add(w[:-1].lower())
        exclamatory_set |= temp
        temp.clear()
    elif w[-1] == '?':
        temp.add(w[:-1].lower())
        interrogative_set |= temp
        temp.clear()
    else:
        temp.add(w.lower())
result = narrative_set & exclamatory_set - interrogative_set
print(f"{' '.join(result)}\n{len(result)}")
