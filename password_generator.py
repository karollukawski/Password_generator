import random
import string

def generate_password(password_length, num_digits, num_lower, num_upper, num_special):
    
    # Determine the remaining characters needed
    num_of_characters_left = password_length - (num_digits + num_lower + num_upper + num_special)

    # Generate random digits
    digits = ''.join(random.choices(string.digits, k=num_digits))

    # Generate random lowercase letters
    lowercase = ''.join(random.choices(string.ascii_lowercase, k=num_lower))

    # Generate random uppercase letters
    uppercase = ''.join(random.choices(string.ascii_uppercase, k=num_upper))

    # Generate random special characters
    special_chars = ''.join(random.choices(string.punctuation, k=num_special))

    # Checking if it is necessary to generate more characters
    if num_of_characters_left > 0:
        option = input("How to fill the rest of password? (digits, lowercase letters, uppercase letters, special characters) ")
        
        # Generate chosen characters for the remaining length
        if option == "digits":
            remaining_chars = ''.join(random.choices(string.digits, k=num_of_characters_left))
        elif option == "lowercase letters":
            remaining_chars = ''.join(random.choices(string.ascii_lowercase, k=num_of_characters_left))
        elif option == "uppercase letters":
            remaining_chars = ''.join(random.choices(string.ascii_uppercase, k=num_of_characters_left))
        elif option == "special characters":
            remaining_chars = ''.join(random.choices(string.punctuation, k=num_of_characters_left))
        else:
            print("Wrong option! Try generate password again.")
            exit()
    else:
        remaining_chars = ""

    # Combine all the generated characters
    password = digits + lowercase + uppercase + special_chars + remaining_chars

    # Shuffle the password to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

# Get user input
password_length = int(input("Enter the desired password length: "))
num_digits = int(input("Enter the number of digits in the password: "))
num_lower = int(input("Enter the number of lowercase letters in the password: "))
num_upper = int(input("Enter the number of uppercase letters in the password: "))
num_special = int(input("Enter the number of special characters in the password: "))

sum = num_digits + num_lower + num_upper + num_special

# Checking if the length of the given password is correct 
if password_length < sum:
    print("More characters than desired length of password! Try generate password again.")
    exit()

# Generate the password
password = generate_password(password_length, num_digits, num_lower, num_upper, num_special)
print("Generated Password:", password)
