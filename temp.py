from collections import Counter

s = 'aaa 111 111 fdg dbb fff bbb bbb daas lk lk lk 12 lk 213 aaa bbb aaa dbb 0 0 0 0 0'
print(Counter.most_common(Counter(s), 3))
