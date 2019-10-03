# Text based fantasy game


#gender = input('Enter your gender: "m" for male, "f" for female. ')

def male_adventure():
    pass

def female_adventure():
    pass




gender = input('Enter your gender: "m" for male, "f" for female. ')
# Converts input to lower
gender = gender.lower()
while gender != 'f' or gender != 'm':
    gender = input('Enter your gender: "m" for male, "f" for female. ')
    gender = gender.lower()
    if gender == 'f':
        female_adventure()
        continue
    elif gender == 'm':
        male_adventure
        continue
    else:
        print('Enter correct option or you "can\'t" play!')
        

# while True:
#     try:
#         rounds_to_play = int(input('How many rounds do you want to play? Enter a number from 1-20: '))

#         if rounds_to_play > 20:
#             print('Please enter a number from 1-20.')
#             continue
#         if rounds_to_play < 1:
#             print('Please enter a number from 1-20')
#         else:
#             break
#     except ValueError:
#         print("Sorry! That was not a valid number. Try again...")