import random

choices = ["Rock", "Paper", "Scissors"]
playerChoice = input("please choose an option \n 1=Rock \n 2=Paper \n 3=Scissors \n Enter your choice: ")

playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error : please choose between 1 and 3!")
else:
    computerChoice = random.randint(1, 3)

    playerChoiceIndex = choices[playerChoice-1]
    computerChoiceIndex = choices[computerChoice-1]

    print("You chose: ", playerChoiceIndex)
    print("Computer chose: ", computerChoiceIndex)

    # Determine the Winner using if else
    if playerChoiceIndex == computerChoiceIndex:
        print("its A Tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("Rocks beats scissors You Win! ")
    elif playerChoice == 2 and computerChoice == 1:
        print("Papers beats rocks You Win! ")
    elif playerChoice == 3 and computerChoice == 2:
        print("Scissors beats papers You Win! ")
    else:
        print("You loose! ")