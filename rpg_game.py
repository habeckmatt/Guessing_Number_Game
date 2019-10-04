# Text based fantasy game

def male_adventure():
    male_name = str(input('Enter your name: '))
    male_name = male_name.capitalize()
    print(male_name)
    queen_name = str(input("What's the name of your queen? "))
    kingdom_name = str(input("What's the name of your kingdom? "))
    allies = str(input("Do you have allies? Enter 'y' for yes or 'n' for no. "))
    allies = allies.lower()
    enemies = str(input("Do you have enemies? Enter 'y' for yes or 'n' for no. "))
    enemies = enemies.lower()
    
    # Only accepts a number as an input.
    while True:
        war_length = input("Enter the war's length: ")
        if war_length.isalpha():
            print("Please enter a number.")
            continue
        else:
            break


    

    if allies == 'y' and enemies == 'y':
        villian_name = str(input(f"{male_name} has a lot of enemies\nEnter your villian's name: "))
        paladin_name = str(input("Enter your paladin's name: "))
        wizard_name = str(input("Enter your wizard's name: "))
        warrior_name = str(input("Enter your warrior's name: "))
        thief_name = str(input("Enter your thief's name: "))
        sorcerer_name = str(input("Enter evil sorcerer's name: "))
        rogue_name = str(input("Enter rogue's name: "))

        print(f"The great {male_name} and his queen {queen_name} peacefully rules the kingdom of {kingdom_name}. 
        However, a great war called Bizarre erupted. {male_name}'s nemesis {villian_name} invaded his kingdom. 
        With the help of {thief_name}, {sorcerer_name}, and {rogue_name}, {villian_name} pillaged their land, 
        stole precious resources, and brutally attacked their villagers.")

        print(f"{male_name} and {queen_name} with the help of {paladin_name}, {wizard_name}, and {warrior_name} 
        valiantly fought back and defeated {villian_name} after {war_length} years of fierce fighting. Order was 
        finally restored and everyone in {kingdom_name} lived happily every after!")

    elif allies == 'y' and enemies == 'n':
        paladin_name = str(input("Enter your paladin's name: "))
        wizard_name = str(input("Enter your wizard's name: "))
        warrior_name = str(input("Enter your warrior's name: "))
        thief_name = str(input("Enter your thief's name: "))
        sorcerer_name = str(input("Enter evil sorcerer's name: "))
        rogue_name = str(input("Enter rogue's name: "))

        print(f"The great {male_name} and his queen {queen_name} peacefully rules the kingdom of {kingdom_name}.")
        print(f"{male_name} and {queen_name} with the help of {paladin_name}, {wizard_name}, and {warrior_name} 
        they keep the peace in their {kingdom_name}!")


    elif allies == 'n' and enemies == 'y':
        villian_name = str(input(f"{male_name} has a lot of enemies\nEnter your villian's name: "))
        paladin_name = str(input("Enter your paladin's name: "))
        wizard_name = str(input("Enter your wizard's name: "))
        warrior_name = str(input("Enter your warrior's name: "))
        thief_name = str(input("Enter your thief's name: "))
        sorcerer_name = str(input("Enter evil sorcerer's name: "))
        rogue_name = str(input("Enter rogue's name: "))

        print(f"The great {male_name} and his queen {queen_name} peacefully rules the kingdom of {kingdom_name}. 
        However, a great war called Bizarre erupted. {male_name}'s nemesis {villian_name} invaded his kingdom. 
        With the help of {thief_name}, {sorcerer_name}, and {rogue_name}, {villian_name} pillaged their land, 
        stole precious resources, and brutally attacked their villagers.")

        print(f"{male_name} and {queen_name} reign has come to an end because they have no help!")


    elif allies == 'n' and enemies == 'n':
        paladin_name = str(input("Enter your paladin's name: "))
        wizard_name = str(input("Enter your wizard's name: "))
        warrior_name = str(input("Enter your warrior's name: "))
        thief_name = str(input("Enter your thief's name: "))
        sorcerer_name = str(input("Enter evil sorcerer's name: "))
        rogue_name = str(input("Enter rogue's name: "))

        print(f"The great {male_name} and his queen {queen_name} peacefully rules the kingdom of {kingdom_name}.")


def female_adventure():
    female_name = str(input('Enter your name: '))
    female_name = female_name.capitalize()
    king_name = str(input("What's the name of your king? "))
    kingdom_name = str(input("What's the name of your kingdom? "))
    allies = str(input("Do you have allies? Enter 'y' for yes or 'n' for no. "))
    allies = allies.lower()
    enemies = str(input("Do you have enemies? Enter 'y' for yes or 'n' for no. "))
    enemies = enemies.lower()
    
    # Only accepts a number as an input.
    while True:
        war_length = input("Enter the war's length: ")
        if war_length.isalpha():
            print("Please enter a number.")
            continue
        else:
            break
    

    if allies == 'y' and enemies == 'y':
        villian_name = str(input(f"{female_name} has a lot of enemies\nEnter your villian's name: "))
        paladin_name = str(input("Enter your paladin's name: "))
        wizard_name = str(input("Enter your wizard's name: "))
        warrior_name = str(input("Enter your warrior's name: "))
        thief_name = str(input("Enter your thief's name: "))
        sorcerer_name = str(input("Enter evil sorcerer's name: "))
        rogue_name = str(input("Enter rogue's name: "))

        print(f"The great {female_name} and his queen {king_name} peacefully rules the kingdom of {kingdom_name}. 
        However, a great war called Bizarre erupted. {female_name}'s nemesis {villian_name} invaded his kingdom. 
        With the help of {thief_name}, {sorcerer_name}, and {rogue_name}, {villian_name} pillaged their land, 
        stole precious resources, and brutally attacked their villagers.")

        print(f"{female_name} and {king_name} with the help of {paladin_name}, {wizard_name}, and {warrior_name} 
        valiantly fought back and defeated {villian_name} after {war_length} years of fierce fighting. Order was 
        finally restored and everyone in {kingdom_name} lived happily every after!")

    elif allies == 'y' and enemies == 'n':
        paladin_name = str(input("Enter your paladin's name: "))
        wizard_name = str(input("Enter your wizard's name: "))
        warrior_name = str(input("Enter your warrior's name: "))
        thief_name = str(input("Enter your thief's name: "))
        sorcerer_name = str(input("Enter evil sorcerer's name: "))
        rogue_name = str(input("Enter rogue's name: "))

        print(f"The great {female_name} and his queen {king_name} peacefully rules the kingdom of {kingdom_name}.")
        
        print(f"{female_name} and {king_name} with the help of {paladin_name}, {wizard_name}, and {warrior_name} 
        they keep the peace in their {kingdom_name}!")


    elif allies == 'n' and enemies == 'y':
        villian_name = str(input(f"{female_name} has a lot of enemies\nEnter your villian's name: "))
        paladin_name = str(input("Enter your paladin's name: "))
        wizard_name = str(input("Enter your wizard's name: "))
        warrior_name = str(input("Enter your warrior's name: "))
        thief_name = str(input("Enter your thief's name: "))
        sorcerer_name = str(input("Enter evil sorcerer's name: "))
        rogue_name = str(input("Enter rogue's name: "))

        print(f"The great {female_name} and his queen {king_name} peacefully rules the kingdom of {kingdom_name}. 
        However, a great war called Bizarre erupted. {female_name}'s nemesis {villian_name} invaded his kingdom. 
        With the help of {thief_name}, {sorcerer_name}, and {rogue_name}, {villian_name} pillaged their land, 
        stole precious resources, and brutally attacked their villagers.")

        print(f"{female_name} and {king_name} reign has come to an end because they have no help!")


    elif allies == 'n' and enemies == 'n':
        paladin_name = str(input("Enter your paladin's name: "))
        wizard_name = str(input("Enter your wizard's name: "))
        warrior_name = str(input("Enter your warrior's name: "))
        thief_name = str(input("Enter your thief's name: "))
        sorcerer_name = str(input("Enter evil sorcerer's name: "))
        rogue_name = str(input("Enter rogue's name: "))

        print(f"The great {female_name} and his queen {king_name} peacefully rules the kingdom of {kingdom_name}.")

# User enters gender. Accepting only m or f for gender.
while True:
    gender = input('Enter your gender: "m" for male, "f" for female. ')
    gender = gender.lower()

    if gender == 'f':
        female_adventure()
        break
    elif gender == 'm':
        male_adventure()
        break
    else:
        print('Enter correct option or you "can\'t" play!')
        

