# sourcery skip: remove-pass-elif
"""
This is a program that counts the number of letters in someone's name. It can take full names by ignoring spaces. 

Things to improve: 
    There's a lot of elif statements in this code that could probably be written more concisely.
"""

from num2words import num2words

username = input("Hello. What's your name?  ")

# Initialize counter for letters in name 
letters = 0

# Checks that name is valid, returns false if anything other than a letter is detected 
validname = True

for character in username: 
    # Only count letters, filtered using ASCII values, ord() function 
    # Upper case 
    if ord(character) >= 65 and ord(character) <= 90 :
            letters +=1

    # Lower case 
    elif ord(character) >= 97 and ord(character) <= 122: 
            letters+=1

    # Don't include spaces
    elif ord(character) == 32:
        # do nothing
        pass

    else:
        print("Invalid character input.")
        validname = False
        # Breaks out of the entire loop if this condition executes 
        break


if validname: 
    print(f"There are {num2words(letters)} letters in your name.")


    
