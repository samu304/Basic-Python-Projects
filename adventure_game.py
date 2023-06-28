user = input("Enter your name: ")
print("Hello ",user)
print("Welcome to the Adventure Game !! \n")

def start_game():
    print("You just waked up and found yourself locked in a mysterious room with two doors \n")
    print("What do you do ? ")
    print("1. Go to Left door.")
    print("2. Go to Right door.")

    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        go_left()
    elif choice == "2":
        go_right()
    else:
        print("Invalid Choice. Try again.")
        start_game()


def go_left():
    print("You enter a dark room with a glowing chest.\n")
    print("What do u do?")
    print("1. Open the Chest.")
    print("2. Leave the room.")

    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        print("Congratulations! You found a treasure.\n")
        play_again()
    elif choice == "2":
        print("You leave the room and go back to the starting point.\n")
        start_game()
    else:
        print("Invalid Choice. Try again.")
        go_left()


def go_right():
    print("You find yourself in a garden eith a locked gate.\n")
    print("What do u do?")
    print("1. Look for a key.")
    print("2. Try to climb over the gate.")

    choice = input("Enter your cjoice (1/2): ")
    if choice == "1":
        print("You find a hidden key under a flower pot.\n")
        unlock_gate()
    elif choice == "2":
        print("You attempted to climb the gate but u slipped and Failed.\n")
        start_game()
    else:
        print("Invalid Choice. Try again.")
        go_right()


def unlock_gate():
    print("You unloacked the gate and stepped into a beautiful garden.\n")
    print("What do u do?")
    print("1. Explore the garden.")
    print("2. Leave the garden.")

    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        print("You discovered a hidden path leading u to a cave.\n")
        enter_cave()
    elif choice == "2":
        print("You decided to leave the garden and go back to the starting point.\n")
        start_game()
    else:
        print("Invalid Choice. Try again.")
        unlock_gate()


def enter_cave():
    print("You enter a dark cave with two tunnels.\n")
    print("What do u do?")
    print("1. Take the left tunnel.")
    print("2. Take the right tunnel.")

    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        print("You find a sleeping dragon. You manage to sneak and pass it.\n")
        find_treasure()
    elif choice == "2":
        print("You encounter a swarn of bats and have to retreat.\n")
        unlock_gate()
    else:
        print("Invalid Choice. Try again.")
        enter_cave()


def find_treasure():
    print("You discovered a hidden treasure in the cave! ")
    print("Congratulations! You've successfully completed the adventure.\n")
    play_again()


def play_again():
    choice = input("Do you want to play again? (y/n): ")
    if choice.lower() == "yes" or choice.lower() == "y":
        start_game()
    else:
        print("Thank you for playing! ")

start_game()
