n, p, q = map(int, input().split())
a = list(map(int, input().split()))
a = a[q:] + a[:q]
a = a[:n // 2][p:] + a[:n // 2][:p] + a[n // 2:][p:] + a[n // 2:][:p]
print(' '.join(map(str, a)))
