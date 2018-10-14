a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

twos = list(range(2, 50, 2))
fives = list(range(5, 100, 5))

c = [2, 2, 2, 7, 8, 9]
d = [2, 5, 10, 2, 19, 98, 104]

common1 = list([])

for elem in a and b: # produces duplicate elements in a new common list if both lists
    if elem in a and elem in b: # have the same number appear multiple times
        common1.append(elem)

print(common1)

common2 = list([])

for elem2 in a:
    if elem2 in b and elem2 not in common2:
        common2.append(elem2)

print(common2)

print(list({x for x in a for y in b if x == y})) # using set comprehensions

print(list(set(a) & set(b)))