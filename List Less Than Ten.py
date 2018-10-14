a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = int(input("Give a number: "))

new_list = []
for value in a:
    if value < number:
        new_list.append(value)

print(new_list)


print(a[0:a.index(5)])

a_new = []
for element in a:
    if element < 5:
        a_new.append(element)

print(a_new)