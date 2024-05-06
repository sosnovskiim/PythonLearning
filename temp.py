def linear_search(a: list[int], value: int):
    n = len(a)
    for i in range(n):
        if a[i] == value:
            return i
    return False


a = [6, -1, 4, 0, 12, -21, 7]
value = 12
print(linear_search(a, value))
