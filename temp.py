def z_func(s):
    n = len(s)
    if n == 0:
        return []
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        else:
            z[i] = 0
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z


def main():
    s_main = input()
    m = int(input())
    queries = [input() for _ in range(m)]

    total_count = 0
    n_main = len(s_main)

    for p in queries:
        l_val = len(p)
        if l_val < 2:
            continue

        # Step 1: pref array
        t1 = p + '#' + s_main
        Z1 = z_func(t1)
        len_t1 = len(t1)

        best_z1 = [10 ** 9] * (l_val + 2)
        best_z1[l_val + 1] = 10 ** 9

        for idx in range(len(p) + 1, len_t1):
            len_match = Z1[idx]
            if len_match != 0 and idx < best_z1[len_match]:
                best_z1[len_match] = idx

        for i in range(l_val, 0, -1):
            if best_z1[i] > best_z1[i + 1]:
                best_z1[i] = best_z1[i + 1]

        # Step 2: suff array
        p_rev = p[::-1]
        s_rev = s_main[::-1]
        t2 = p_rev + '#' + s_rev
        Z2 = z_func(t2)
        len_t2 = len(t2)

        best_z2 = [10 ** 9] * (l_val + 2)
        best_z2[l_val + 1] = 10 ** 9

        for idx in range(len(p_rev) + 1, len_t2):
            len_match = Z2[idx]
            if len_match != 0 and idx < best_z2[len_match]:
                best_z2[len_match] = idx

        for i in range(l_val, 0, -1):
            if best_z2[i] > best_z2[i + 1]:
                best_z2[i] = best_z2[i + 1]

        # Step 3: Check condition
        found = False
        for i in range(1, l_val):
            j = l_val - i
            if best_z1[i] == 10 ** 9 or best_z2[j] == 10 ** 9:
                continue
            # start_pref = best_z1[i] - (l_val + 1)
            # end_suff = n_main + l_val - best_z2[j]
            # if end_suff >= start_pref + l_val - 1:
            #     found = True
            #     break
            if n_main + l_val - best_z2[l_val - i] >= best_z1[i] - 2:
                found = True
                break

        if found:
            total_count += 1

    print(total_count)


if __name__ == "__main__":
    main()