import random 

attempts = 0
randnum = random.randint(0,100)

print("Computer choice a number between 0-100")

while True:
    guess = int(input("Enter your Guess:"))
    
    if guess == randnum:
        print("Wow! Congrulations You FOUND! Number was {} and you found at your {}. attempt.".format(randnum, attempts))
        break
    elif guess < randnum:
        print("Number is higher than this! Try Again.")
        attempts +=1 
    elif guess > randnum:
        print("Number is lower than this! Try Again.")
        attempts +=1 

        


