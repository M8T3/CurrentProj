def get_number(prompt="Give me a number >= 2: "):
    return int(input(prompt))


number = get_number()

num_range = list(range(2, number+1))


def check_prime(integer):
    return int(number % integer)


for elem in num_range:
    remainder = check_prime(elem)
    if remainder == 0 and elem != 2 and elem != number:
        print(str(number) + " is not a prime number.")
        break
    elif number == elem:
        print(str(number) + " is a prime number.")
        break





   




