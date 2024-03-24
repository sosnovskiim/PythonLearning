def secret_replace(text, **rules):
    res = ''
    cnt = {c: 0 for c in rules.keys()}
    for char in text:
        if char in rules:
            cnt[char] += 1
            res += rules[char][cnt[char] % len(rules[char]) - 1]
        else:
            res += char
    return res


if __name__ == '__main__':
    result = secret_replace(
        "ABRA-KADABRA",
        A=("Z", "1", "!"),
        B=("3",),
        R=("X", "7"),
        K=("G", "H"),
        D=("0", "2"),
    )
    print(f'result = {result}')
