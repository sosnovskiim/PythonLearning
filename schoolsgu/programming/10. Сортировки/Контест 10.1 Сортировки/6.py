with open('input.txt', 'r') as file_in:
    n = int(file_in.readline())
    a = [[int(i) for i in row.split()] for row in file_in.readlines()]
    for j in range(n):
        if (j + 1) % 2 == 0:
            for i in range(1, n):
                k = i
                while k > 0 and a[k][j] > a[k - 1][j]:
                    a[k][j], a[k - 1][j] = a[k - 1][j], a[k][j]
                    k -= 1
        else:
            for i in range(1, n):
                k = i
                while k > 0 and a[k][j] < a[k - 1][j]:
                    a[k][j], a[k - 1][j] = a[k - 1][j], a[k][j]
                    k -= 1
with open('output.txt', 'w') as file_out:
    for row in a:
        file_out.write(f'{" ".join(str(i) for i in row)}\n')
