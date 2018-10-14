name = input("Give name: ")
print("Your name is " + name)

age = int(input("Enter your age: "))
print("You are " + str(age) + " years old")

birth_year = 2018 - age
old_year = str(birth_year + 100)
print("You will turn 100 years old in " + old_year)

Number = int(input("Give me you favorite number: "))
print(Number *("You will turn 100 years old in " + old_year + " "))
print(Number * ("You will turn 100 years old in " + old_year + "\n"))
