def can_eat(knight, figure):
    dx, dy = abs(knight[0] - figure[0]), abs(knight[1] - figure[1])
    return dx == 2 and dy == 1 or dx == 1 and dy == 2


if __name__ == '__main__':
    result = can_eat((2, 1), (4, 2))
    print(f'result = {result}')
