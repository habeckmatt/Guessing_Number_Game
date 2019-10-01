## This is a guess the number game
import random

guessesTaken = 0

print("Hello! What is your name?")
while True:
        myName = input()
        if not myName.isalpha():
            print("Enter only alphabetical characters for you name. Please enter you name again: ")
            continue

        else:
            break

print("Well hello " f'{myName}' + ", I am thinking of a number between 1 and 100. Take a guess!")

number = random.randint(1,100)



while guessesTaken < 4:
    
    guess = input()
    guess = int(guess)
    guessesTaken += 1
    
    if guess < number:
        print("The number you guessed is too low, try again!")

    if guess > number:
        print("The number you guessed is too high, try again!")

    if guess == number:
        print("Congrats you've done it!\nIt took you " f'{guessesTaken}' + " to guesses to guess the number!")
        exit()
        

if guessesTaken == 4:
    print("This is your last guess, make it count! Enter it now:")
    guess = input()
    guess = int(guess)
    guessesTaken += 1
    
       
if guess == number:
    guessesTaken = str(guessesTaken)
    print("Congrats you've done it!\nIt took you " f'{guessesTaken}' + " to guesses to guess the number!")

if guess != number:
    print("Sorry that wasn't the number I was thinking of.\nThe number I was thinking of was " + f'{number}' + ".")
