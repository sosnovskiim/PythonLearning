dm = {1: 'spades', 2: 'clubs',
      3: 'diamonds', 4: 'hearts'}
dk = {14: 'ace', 13: 'king', 12: 'queen',
      11: 'jack', 10: 'ten', 9: 'nine',
      8: 'eight', 7: 'seven', 6: 'six'}
m, k = map(int, input().split())
print(f'the {dk[k]} of {dm[m]}')
