def reverse_string():
    words = str(input("Type an expression: "))
    gaps = words.split()
    reverse = gaps[::-1]
    reverse_list = " ".join(reverse)
    return reverse_list


a = reverse_string()
print(a)