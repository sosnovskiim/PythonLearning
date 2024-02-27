n = int(input())
cnt1, cnt2, cnt3 = 0, 0, 0
while True:
    t = int(input())
    if t == -2 * 10 ** 9:
        break
    if t > n:
        cnt1 += 1
    elif t < n:
        cnt2 += 1
    else:
        cnt3 += 1
    n = t
if cnt1 > 0 and cnt2 == 0:
    if cnt3 == 0:
        print('ASCENDING')
    else:
        print('WEAKLY ASCENDING')
elif cnt1 == 0 and cnt2 > 0:
    if cnt3 == 0:
        print('DESCENDING')
    else:
        print('WEAKLY DESCENDING')
elif cnt1 == 0 and cnt2 == 0:
    print('CONSTANT')
else:
    print('RANDOM')
