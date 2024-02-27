n = int(input())
if n % 3 == 0 and n % 10 == 3 or n % 3 != 0 and n % 10 != 3:
    print(0)
else:
    print(1)
