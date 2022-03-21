import string
import random

SPECIAL_CHARS = list('!@#$%^&*()')
UPPER_CHARS     = list(string.ascii_letters.upper())
LOWER_CHARS = list(string.ascii_letters)
DIGITS = list(string.digits)

# print (SPECIAL_CHARS + UPPER_CHARS + LOWER_CHARS + DIGITS)

def generate_random_pass():
    
    # User Inputs
    length = int(input('What is your desired passsword legnth: '))

    if length <= 8:
        print ('ERROR: For your security ensure password length is greater than 8 characters')

        length = int(input('What is your desired passsword legnth: '))

    ## TODO: Allow the user to choose how many letters, numbers, and punctuation characters they want in their password. Mix everything up using list(), random.shuffle(), and ''.join(). 

    password =[]
    i=0
    while i < length+1:
    # for i in range(length):
        password.append(random.choice(SPECIAL_CHARS + UPPER_CHARS + LOWER_CHARS + DIGITS))

    # convers randomizes password and converts to a string for user to copy
    random.shuffle(password)
    print("".join(password))

    
generate_random_pass()