with open('input.txt', 'r') as file_in:
    n = int(file_in.readline())
    a = list()
    product, company, quantity = 'product', 'company', 'quantity'
    for i in range(n):
        p, c, q = file_in.readline().split()
        a.append({product: p, company: c, quantity: q})
        j = i
        while j > 0 and (p < a[j - 1][product] or (
            p == a[j - 1][product] and int(q) > int(a[j - 1][quantity])
        )):
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
    e = file_in.readline()
with open('output.txt', 'w') as file_out:
    i = 0
    while i < 10 and i < len(a):
        if a[i][company] != e:
            file_out.write(f'{" ".join(a[i].values())}\n')
        i += 1
