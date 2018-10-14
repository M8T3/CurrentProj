game = input('Type "start" to start a new game or "quit" to cancel: ')

while game != "start":
    if game == "quit":
        print("Good game!")
        break
    else:
        print("Invalid response")
        game = input('Type "start" to start a new game or "quit" to cancel: ')

while game == "start":
    p1 = input('Enter your name player 1: ')
    p2 = input('Enter your name player 2: ')
    p1choice = input('Enter rock, paper, or scissors, player 1: ')
    p2choice = input('Enter rock, paper, or scissors, player 2: ')
    if p1choice == "rock" and p2choice == "scissors":
        print(p1, "wins!")
        game = input('Type "start" to start a new game or "quit" to cancel: ')
        if game == "quit":
            print("Good game!")
        else:
            print("Invalid response")
            game = input('Type "start" to start a new game or "quit" to cancel: ')
    elif p1choice == "scissors" and p2choice == "paper":
        print(p1, "wins!")
        game = input('Type "start" to start a new game or "quit" to cancel: ')
        if game == "quit":
            print("Good game!")
        else:
            print("Invalid response")
            game = input('Type "start" to start a new game or "quit" to cancel: ')
    elif p1choice == "paper" and p2choice == "rock":
        print(p1, "wins!")
        game = input('Type "start" to start a new game or "quit" to cancel: ')
        if game == "quit":
            print("Good game!")
        else:
            print("Invalid response")
            game = input('Type "start" to start a new game or "quit" to cancel: ')
    elif p1choice == p2choice:
        print("It's a tie!")
        game = input('Type "start" to start a new game or "quit" to cancel: ')
        if game == "quit":
            print("Good game!")
        else:
            print("Invalid response")
            game = input('Type "start" to start a new game or "quit" to cancel: ')
    elif p2choice == "rock" and p1choice == "scissors":
        print(p2, "wins!")
        game = input('Type "start" to start a new game or "quit" to cancel: ')
        if game == "quit":
            print("Good game!")
        else:
            print("Invalid response")
            game = input('Type "start" to start a new game or "quit" to cancel: ')
    elif p2choice == "scissors" and p1choice == "paper":
        print(p2, "wins!")
        game = input('Type "start" to start a new game or "quit" to cancel: ')
        if game == "quit":
            print("Good game!")
        else:
            print("Invalid response")
            game = input('Type "start" to start a new game or "quit" to cancel: ')
    elif p2choice == "paper" and p1choice == "rock":
        print(p2, "wins!")
        game = input('Type "start" to start a new game or "quit" to cancel: ')
        if game == "quit":
            print("Good game!")
        else:
            print("Invalid response")
            game = input('Type "start" to start a new game or "quit" to cancel: ')
    elif p1choice != "rock" or "paper" or "scissors" or p2choice != "rock" or "paper" or "scissors":
        print("Invalid response")
        game = input('Type "start" to start a new game or "quit" to cancel: ')




