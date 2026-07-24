import random
choices = ["snake","water", "gun"]
while True:
    computer = random.choice(choices)

    user = input("enter your choice snake,water,gun:")
    print("computer choice is:", computer)
    print("user choice is:", user)
    if user not in choices:
        print(" Invalid input! Please enter snake, water, or gun.")
    elif computer == user:
        print("it's a tie")
    elif computer == "snake" and user == "water":
        print("computer wins")
    elif computer == "water" and user == "gun":
        print("computer wins")
    elif computer == "gun" and user == "snake":
        print("computer wins")
    else:
        print("user wins")
    print("Thanks for playing the game!")
    play_again = input("Do you want to play again? (yes/no): ").lower
    if play_again != "yes":
        print("thanks for playing the game!")
        break