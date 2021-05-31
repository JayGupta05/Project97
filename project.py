number = "5"
chance = 5
print("Welcome to the number guessing game!!")
guess=""

while chance >= 1:
    print("Guess a number between 1-9")
    guess = input("Enter Your Guess - ")
    chance = chance-1
    if(guess < number):
        print("Your guess is too low. Guess something higher.")
    elif(guess > number):
        print("Your guess is too high. Guess something lower.")
    elif(guess == number):
        print("You Win!!")
        break

if (chance < 1):
    print("You Lose!! The correct number was " + number)