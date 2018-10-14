def list_ends(elem):
    return elem[0:len(elem):len(elem)-1]


def list_bookends(elem):
    return [x for x in elem if x is elem[0] or x is elem[len(elem)-1]]


a = [5, 10, 15, 20, 25]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = list(list_ends(b))
print(new_list)

another_list = list(list_bookends(b))
print(another_list)

