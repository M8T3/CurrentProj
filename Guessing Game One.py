import random

n = random.randint(1,9)

game = str(input("Enter 'start' to play the guessing game and 'exit' to stop: "))

tries = 0

while game != 'start':
    if game == 'exit':
        print("You made", tries, "guesses")
        break
    else:
        print("Invalid response")
        game = str(input("Enter 'start' to play the guessing game and 'exit' to stop: "))

while game == 'start':
    guess = int(input("Please guess a number between 1 and 9: "))
    if guess == n:
        print("You guessed the number correctly!")
        tries += 1
        n = random.randint(1, 9)
        game = str(input("Enter 'start' to play the guessing game and 'exit' to stop: "))
        if game == 'exit':
            print("You made", tries, "guesses")
            break
    elif n > guess:
        print("You guessed too low.")
        tries += 1
    elif n < guess:
        print("You guessed too high.")
        tries += 1