def number_length(n):
    return len(str(abs(n)))


if __name__ == '__main__':
    result = number_length(12345)
    print(f'result = {result}')
