number = int(input("Give me a number: "))

num_range = list(range(1, number))

print("These are the divisors of", number)
divisors = []

for x in num_range:
    if number % x is 0:
        divisors.append(x)

print(divisors)
