import string
import random

#  password length
length = int(input("Enter password length: "))

print('''Choose character set for password from these : 
		1. Digits
		2. Letters
		3. Special characters
		4. Exit''')

characterList = ""

# character set for password
while (True):
    choice = int(input("Pick a number "))
    if (choice == 1):

        # Adding letters 
        characterList += string.ascii_letters
    elif (choice == 2):

        # Adding digits 
        characterList += string.digits
    elif (choice == 3):

        # Adding special characters 
        
        characterList += string.punctuation
    elif (choice == 4):
        break
    else:
        print("Please pick a valid option!")

password = []

for i in range(length):
    # character list
    randomchar = random.choice(characterList)

    # adding a random character to password
    password.append(randomchar)

# displaying password as a string
print("The random password is " + "".join(password))
