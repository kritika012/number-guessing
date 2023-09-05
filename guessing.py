import random

randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if (userGuess == randNumber):
        print("you guessed right!")
    else:
        if(userGuess > randNumber):
            print("You guessed it wrong! Lower number please")
        else:
            print("you guessed it wrong! Higher number please")

print(f"you guessed it in {guesses} guesses")