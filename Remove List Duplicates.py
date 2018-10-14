def unique_list(data):
    menu = list(data)
    new_list = []
    for item in menu:
        if item not in new_list:
            new_list.append(item)

    print(new_list)


op = [1, 1, 1, 3, 6, 7, 9, 9, 5]
a = unique_list(op)


def special_list(info):
    order = list(set(info))
    print(order)


b = special_list(op)
