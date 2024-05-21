with open('input.txt', 'r', encoding='utf-8') as file_in:
    n = int(file_in.readline())
    a = list()
    product, company, quantity = 'product', 'company', 'quantity'
    for i in range(n):
        p, c, q = file_in.readline().strip().split()
        a.append({product: p, company: c, quantity: q})
        j = i
        while j > 0 and (p < a[j - 1][product] or (
                p == a[j - 1][product] and int(q) > int(a[j - 1][quantity])
        )):
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
    e = file_in.readline()
with open('output.txt', 'w', encoding='utf-8') as file_out:
    cnt, i, t = 0, 0, []
    while cnt < 10 and i < len(a):
        if a[i][company] != e:
            t.append(a[i])
            cnt += 1
        i += 1
    file_out.write('\n'.join(' '.join(i.values()) for i in t))
