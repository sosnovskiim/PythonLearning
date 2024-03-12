def remove_opposite(a):
    d = dict()
    i = 0
    while i < len(a):
        n = a[i]
        if -n in d:
            a.pop(i)
            i -= 1
            a.pop(d[-n])
            d.pop(-n)
        else:
            d[n] = i
            i += 1


numbers = [int(i) for i in input().split()]
remove_opposite(numbers)
print(' '.join(map(str, numbers)))
