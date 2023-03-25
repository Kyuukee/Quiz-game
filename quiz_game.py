print("Welcome to my computer quiz!")


while True:
    playing = input("Do you want to play?: ")
    if playing.lower() == "yes":
        print("OKAY LETS PLAY!\n")
        break
    else:
        print("That wasn't a real question...")


def quiz():
    while True:
        answer = input("What does CPU stand for?: ")
        if answer.lower() == "central processing unit":
            print("That is correct!")
            break
        else:
            print("That is incorrect, please try again\n")

    while True:
        answer = input("What does GPU stand for?: ")
        if answer.lower() == "graphics processing unit":
            print("That is correct!")
            break
        else:
            print("That is incorrect, please try again\n")

    while True:
        answer = input("What does RAM stand for?: ")
        if answer.lower() == "random access memory":
            print("That is correct!\n")
            break
        else:
            print("That is incorrect, please try again\n")

    while True:
        leave = input("Would you like to play again?: ")

        if leave.lower() == "no":
            print("Thanks for playing\n\n")
            time.sleep(1)
            print("Exiting in 3...\n\n")
            time.sleep(1)
            print("2...\n\n")
            time.sleep(1)
            print("1...\n\n")
            time.sleep(1)
            print("GOODBYE!!!")
            time.sleep(1)
        else:
            print("\nPress ENTER to play again")
            time.sleep(1)
            input()
            quiz()

