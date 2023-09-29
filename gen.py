import os
import random
import string
os.system("clear")

def generate_password(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))

def generate_passwords(length, quantity, password_type):
    passwords = []
    if password_type == "Digits":
        chars = string.digits
        for _ in range(quantity):
            password = generate_password(length, chars)
            passwords.append(password)
    elif password_type == "random Year first then random 2 number":
        for _ in range(quantity):
            year = random.randint(2002, 2010)
            number = random.randint(0, 20)
            password = str(year) + str(number).zfill(2)
            passwords.append(password)
    elif password_type == "Random person name then # / @ / $ random 3 number":
        chars = string.ascii_letters
        symb = input("  SYMBOLS [SEPARATED BY COMMA] : ")
        symbols = ['', '', '', '$', '']
        symbols += symb.split(', ')

        nms = input("Target names eg.(Z3R0, Trace, PassWord) : ")
        # add your own target names/keywords here bro
        names = ['Pass', 'Password', '', '', 'Pass123']
        names += nms.split(', ')
        for _ in range(quantity):
            name = random.choice(names)
            symbol = random.choice(symbols)
            number = random.randint(0, 999)
            password = name + symbol + str(number).zfill(3)
            passwords.append(password)
    elif password_type == "Random letters":
        chars = string.ascii_letters
        for _ in range(quantity):
            password = generate_password(length, chars)
            passwords.append(password)

    return passwords

length = 6
quantity = 15000

# REMOVE HASH TAG TO TURN IT ON
#password_type = "Digits"
#passwords_1 = generate_passwords(length, quantity, password_type)

# Generate passwords of type "random Year first then random 2 number"
password_type = "random Year first then random 2 number"
passwords_2 = generate_passwords(length, quantity, password_type)
# Generate passwords of type "Random person name then # / @ / $ random 3 number"
password_type = "Random person name then # / @ / $ random 3 number"
passwords_3 = generate_passwords(length, quantity, password_type)

# REMOVE HASHTAG IF U WANT TO Generate passwords of type "Random letters"
#password_type = "Random letters"
#passwords_4 = generate_passwords(length, quantity, password_type)

# Combine all generated passwords YOU CAN ADD MORE HERE
all_passwords = passwords_2 + passwords_3

# Shuffle the passwords
random.shuffle(all_passwords)

# Save all generated passwords to pass.txt
with open("pass.txt", "w") as file:
    for password in all_passwords:
        file.write(password + "\n")
