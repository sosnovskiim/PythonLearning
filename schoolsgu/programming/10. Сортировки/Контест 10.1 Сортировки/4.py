with open('input.txt', 'r') as file_in:
    n = int(file_in.readline())
    m = list()
    for row in file_in.readlines():
        m.append(sorted((int(i) for i in row.split()), reverse=True))
with open('output.txt', 'w') as file_out:
    for row in m:
        file_out.write(f'{" ".join(str(i) for i in row)}\n')
