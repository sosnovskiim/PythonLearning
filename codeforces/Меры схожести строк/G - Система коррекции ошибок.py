from collections import defaultdict

n = int(input())
s = input()
t = input()
base = sum(1 for a, b in zip(s, t) if a != b)
if base == 0:
    print(0)
    print(-1, -1)
    exit()
diff_pos = {i for i in range(n) if s[i] != t[i]}
pair_dict = {}
for i in diff_pos:
    key = (t[i], s[i])
    if key in pair_dict:
        print(base - 2)
        print(i + 1, pair_dict[key] + 1)
        exit()
    pair_dict[(s[i], t[i])] = i
needed_chars = defaultdict(list)
for i in diff_pos:
    needed_chars[t[i]].append(i)
for i in diff_pos:
    if s[i] in needed_chars:
        for j in needed_chars[s[i]]:
            if j != i:
                print(base - 1)
                print(i + 1, j + 1)
                exit()
print(base)
print(-1, -1)
