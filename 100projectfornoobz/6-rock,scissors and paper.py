import random
print(("*"*30) + "\n Rock, Paper, Scissors \n" + ("*"*30) )
user_score, computer_score = 0,0

while user_score<=2 and computer_score<=2:
    print ("Select Your Move:\n1-Rock\n2-Paper\n3-Scissors")
    user_selection = input("Your Choice:" )
    computer_selection= random.choice(["1","2","3"])

    if user_selection == "1":
        if computer_selection == "1":
            print("Computer's Choice is rock. Rock equal to Rock! No score!")
        elif computer_selection == "2":
            print ("Computer's Choice is Paper. Paper wraps Rock. You Lose!")
            computer_score+=1
        elif computer_selection == "3":
            print("Computer's Choice is Scissors. Rock breaks Scissors. You win!")
            user_score+=1
    elif user_selection == "2":
        if computer_selection == "1":
            print("Computer's choice: Rock\nPaper wraps stone. You win!")
            user_score += 1
        elif computer_selection == "2":
            print("Computer's choice: Paper\nPaper equal to paper. Scoreless!")
        elif computer_selection == "3":
            print("Computer's choice: Scissors\nScissors cuts paper. You lose!")
            computer_score += 1
    elif user_selection == "3":
        if computer_selection == "1":
            print("Computer's choice: Rock\nRock breaks scissors. You lose!")
            computer_score += 1
        elif computer_selection == "2":
            print("Computer's choice: Paper\nScissors cuts paper. You win!")
            user_score += 1
        elif computer_selection == "3":
            print("Computer's choice: Scissors\nScissors equal to scissors. Scoreless!")
    else:
        break

print("\n Match Score: You:{}-Com:{}".format(user_score, computer_score))
