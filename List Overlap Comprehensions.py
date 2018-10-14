import random
from collections import Counter

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = random.randint(1, 100)
d = random.randint(1, 100)
e = random.sample(range(100), c)
f = random.sample(range(100), d)

cmn_list = []

cmn_list = [num for num in e if num in f if num not in cmn_list]

for elem in cmn_list:
    cmn_list.count(elem)
    if cmn_list.count(elem) > 1:
        cmn_list.remove(elem)

print(cmn_list)

g = list(Counter(cmn_list))
print(g)