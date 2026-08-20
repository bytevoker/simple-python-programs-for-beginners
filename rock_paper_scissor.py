# Can you win against this program?

# You choose one option among Rock, Paper, and Scissor. This program also does the same.

# Rules of the game:
#       Paper beats Rock
#       Rock beats Scissor
#       Scissor beats Paper

import random

while True:

    # Program's choice.
    rndm = random.randint(1,3)
    if rndm == 1:
       prgm = 'rock'
    elif rndm == 2:
       prgm = 'paper'
    else:
       prgm = 'scissor'

    # User's choice.
    usr_inpt = input("Enter: \n\t'R' or 'r' for Rock\n\t'P' or 'p' for Paper\n\t'S' or 's' for Scissor\n").lower().strip()

    if usr_inpt in ['r', 's', 'p']:
        if usr_inpt == 'r':
            usr = 'rock'
        elif usr_inpt == 'p':
            usr = 'paper'
        else:
            usr = 'scissor'

        print(f"You:{usr}\tComputer:{prgm}\n")
        # Matching the possible cases.
        match usr:
            case _ if usr == prgm:
                print("********** It's a draw! **********")
            case _ if usr[0] == 'r' and prgm[0] == 'p':
                print("********** You lose! **********")
            case _ if usr[0] == 'r' and prgm[0] == 's':
                print("********** You won! **********")
            case _ if usr[0] == 'p' and prgm[0] == 'r':
                print("********** You won! **********") 
            case _ if usr[0] == 'p' and prgm[0] == 's':
                print("********** You lose! **********")
            case _ if usr[0] == 's' and prgm[0] == 'p':
                print("********** You won! **********")
            case _ if usr[0] == 's' and prgm[0] == 'r':
                print("********** You lose! **********")
    else:
        print("Invalid Input!")
 
    #This part tells the program whether to stop the program or not.
    while True:
        choice = input("\nDo you want to continue?\nPress:\n\t\"y\" for Yes\n\t\"n\" for No\n").strip().lower()
        if choice == "y":
            break
        elif choice == "n":
            break
        else:
            print("Invalid Input!")

    if choice == "n":
        print("Program successfully ended!")
        break
    