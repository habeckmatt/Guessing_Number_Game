
MAX_KEY_SIZE = 26

def getMode():

    # Loops until user inputs Encrypt, e, decrypt or d
    while True:
        print("Do you wish to encrypt or decrypt a message?")

        mode = input().lower()

        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print("Enter either 'Encrypt' or 'e' or 'decrypt' or 'd'.")

def getMessage():
    # User enters the message they wish to encrypt/decrypt
    message = input("Enter your message: ")
    return message

def getKey():
    key = 0
    # User enters the key size they would like to use between 1 and 26
    while True:
        print("Enter the key number 1-"f'{MAX_KEY_SIZE}'":")
        key = int(input())
        if (key>=1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    # key = -key alerts program if we want to decrpyt the message
    if mode[0] == 'd':
         key = -key
    translated=''

    # Conditions that make the message encrypted or decrypted based upon location
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -=26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

# Calls all of the functions

mode = getMode()
message = getMessage()
key = getKey()


print('Your translated text is: ')
print(getTranslatedMessage(mode,message,key))


