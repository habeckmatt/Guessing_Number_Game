from random import randint
from time import sleep

def three_num_lotto():
    user_guess1 = int(input("Enter your first number: "))
    user_guess2 = int(input("Enter your second number: "))
    user_guess3 = int(input("Enter your third number: "))
    user_guess_list = []
    user_guess_list.append(user_guess1)
    user_guess_list.append(user_guess2)
    user_guess_list.append(user_guess3)

    loto_num1 = randint(0,9)
    loto_num2 = randint(0,9)
    loto_num3 = randint(0,9)
    loto_nums = []
    loto_nums.append(loto_num1)
    loto_nums.append(loto_num2)
    loto_nums.append(loto_num3)

    print(f"Loto ball 1 rolling...")
    sleep(1)
    print(f"Loto ball 2 rolling...")
    sleep(1)
    print(f"Loto ball 3 rolling...")
    sleep(1)

    if user_guess_list == loto_nums:
        print(f"Contrats you are a winner! Your numbers were: {user_guess_list}.\nThe lotto numbers were {loto_nums}.")
    else:
        print(f"I'm sorry, you are not a winner. Your numbers were: {user_guess_list}.\nThe lotto numbers were {loto_nums}.")

    
    while True:
        play_again = str(input("Would you like to play again? Enter 'y' for yes and 'n' for no: "))
        if play_again == 'y':
            break
        elif play_again == 'n':
            print("Thanks for playing!")
            exit()
        else:
            print("Please enter either y for yes or n for no...")


def four_num_lotto():
    user_guess1 = int(input("Enter your first number: "))
    user_guess2 = int(input("Enter your second number: "))
    user_guess3 = int(input("Enter your third number: "))
    user_guess4 = int(input("Enter your fourth number: "))
    user_guess_list = []
    user_guess_list.append(user_guess1)
    user_guess_list.append(user_guess2)
    user_guess_list.append(user_guess3)
    user_guess_list.append(user_guess4)

    loto_num1 = randint(0,9)
    loto_num2 = randint(0,9)
    loto_num3 = randint(0,9)
    loto_num4 = randint(0,9)
    loto_nums = []
    loto_nums.append(loto_num1)
    loto_nums.append(loto_num2)
    loto_nums.append(loto_num3)
    loto_nums.append(loto_num4)

    print(f"Loto ball 1 rolling...")
    sleep(1)
    print(f"Loto ball 2 rolling...")
    sleep(1)
    print(f"Loto ball 3 rolling...")
    sleep(1)
    print(f"Loto ball 4 rolling...")
    sleep(1)

    if user_guess_list == loto_nums:
        print(f"Contrats you are a winner! Your numbers were: {user_guess_list}.\nThe lotto numbers were {loto_nums}.")
    else:
        print(f"I'm sorry, you are not a winner. Your numbers were: {user_guess_list}.\nThe lotto numbers were {loto_nums}.")

    while True:
        play_again = str(input("Would you like to play again? Enter 'y' for yes and 'n' for no: "))
        if play_again == 'y':
            break
        elif play_again == 'n':
            print("Thanks for playing!")
            exit()
        else:
            print("Please enter either y for yes or n for no...")



while True:
    play_game = str(input("Would you like to play the California lottery? Enter 'y' for yes and 'n' for no: "))
    play_game = play_game.lower()

    if play_game == 'y':
        while True:
            try:
                which_game = int(input("Which lottery game would you like to play? Three or four number? Enter '3' for three and '4' for four: "))
                if which_game == 3:
                    three_num_lotto()
                    
                elif which_game == 4:
                    four_num_lotto()
                    
                else:
                    print("Please enter either a '3'or '4'.")
                    continue
            except ValueError:
                print("Sorry you did not enter 3 or 4. Please try again... ")

    elif play_game == 'n':
        print("You don't want to play, we're sad to see you go!")
        exit()
    else:
        print("Please enter either 'y' or 'n'")
        continue