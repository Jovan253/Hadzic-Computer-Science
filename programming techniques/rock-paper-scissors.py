print("Lets play rock paper scissors, First to Three!!!")

print("Enter 1 for rock")
print("Enter 2 for paper")
print("Enter 3 for scissors")

player_score = 0
comp_score = 0

from random import randint
while player_score != 3 or comp_score != 3:
    
    choice = int(input())
    computer_choice = randint(1,3)
    if choice == 1 and computer_choice == 2:
        comp_score += 1
        print("You Lost, Computer Chose Paper, You Chose Rock")
    elif choice == 1 and computer_choice == 3:
        player_score += 1
        print("you Win, Computer Chose Scissors, You Chose Rock")
    elif choice == 2 and computer_choice == 1:
        player_score += 1
        print("You Win, Computer Chose Rock, You Chose Paper")
    elif choice == 2 and computer_choice == 3:
        comp_score += 1
        print("You Lost, Computer Chose Scissors, You Chose Paper")
    elif choice == 3 and computer_choice == 1:
        comp_score += 1
        print("You Lost, Computer Chose Rock, You Chose Scissors")
    elif choice == 3 and computer_choice == 2:
        player_score += 1
        print("You Win, Computer Chose Paper, You Chose Scissors")
    else:
        print("You chose the same thing")
        player_score = player_score
        comp_score = comp_score

    if comp_score == 3:
        print("The Computer Won, Better Luck Next Time")
        break
    elif player_score == 3:
        print("Congrats, You Beat The Computer")
        break
        
    
