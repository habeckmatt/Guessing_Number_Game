from random import randint
from time import sleep


while True:
    try:
        rounds_to_play = int(input('How many rounds do you want to play? Enter a number from 1-20: '))

        if rounds_to_play > 20:
            print('Please enter a number from 1-20.')
            continue
        if rounds_to_play < 1:
            print('Please enter a number from 1-20')
        else:
            break
    except ValueError:
        print("Sorry! That was not a valid number. Try again...")

dice_numbers = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
}

turns_played = 0
correct_guesses = 0

while turns_played < (rounds_to_play):
    turns_played += 1
    
    try:
        dice_roll = int(input('Roll the dice. Enter a number from 1-6... '))
        if dice_roll > 6:
            print('Please enter a number from 1-6.')
            continue
        if dice_roll < 1:
            print('Please enter a number from 1-6.')
            continue

    except ValueError:
        print("Sorry! That was not a valid number. Try again...")
        continue

    print('Dice rolling...')
    dice_result = randint(1,6)
    sleep(1.5)

    if dice_roll == dice_result:
        print('You win! The dice landed on 'f'{dice_result}''.')
        correct_guesses += 1
    if dice_roll != dice_result:
        print('Better luck next time. Dice landed on 'f'{dice_result}''.')

    if dice_result == 1:
        dice_numbers[1] += 1
    if dice_result == 2:
        dice_numbers[2] += 1
    if dice_result == 3:
        dice_numbers[3] += 1
    if dice_result == 4:
        dice_numbers[4] += 1
    if dice_result == 5:
        dice_numbers[5] += 1
    if dice_result == 6:
        dice_numbers[6] += 1

    print('Round: 'f'{turns_played}')

print('------------------------------------')
for key, value in dice_numbers.items():
     print('Dice landed on ' + str(key)+': '+ str(value) + ' times.')
    #print('Dice landed on' x, y 'times.')
print('------------------------------------')

average_correct = correct_guesses/turns_played
print('Correct guesses: 'f'{correct_guesses}')
print('Average of correct guesses: 'f'{average_correct}')
