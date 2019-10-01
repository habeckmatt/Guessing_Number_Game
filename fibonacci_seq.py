# List of the starting fibonacci numbers
n1 = 0
n2 = 1

def gather_sequence():
# Checks that the number taken is not negative, or a decimal.

while True:
    try:
        max_length = int(input("How long of a sequence do you want? "))

        if max_length <= 0:
            print("Please enter a positive integer.")
            continue

        # If the number is 1 print out the sequence
        elif max_length == 1:
            print("Here is your sequence: " f'{n1}')
        else:
            break 
    except ValueError:
        print("Oops! That was not a valid integer. Try again...")


count = 0
# Adds the previous number with the next
def countit():
while count <= (max_length-1):
    print(n1,end=' , ')
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    count += 1

# Prints out the final number
if count == max_length:
    print(n1)
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    count += 1

gather_sequence()  
countit()  
