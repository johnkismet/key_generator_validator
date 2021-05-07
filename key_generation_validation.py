import secrets
import string


def generate_key():
    """ The password is a random set of choices from the alphabet. It should be 10 digits long. It will try to validate the password and only if the validation returns true will the while loop end"""
    password_len = 15
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(password_len))
        if validate_key(password):
            print(f'{password} is valid!')
            return password
        else:
            # print(f'{password} was not valid')
            password = ''
        # if (any(c.islower() for c in password) and any(c.isupper() 
        # for c in password) and sum(c.isdigit() for c in password) >= 3):
            
def validate_key(key):
    """To validate we loop through each char in the key (which is a string). There must be 3 instances of the first char. And the ord of the entire string must == 1337, else validation will be false"""
    score = 0
    check_char = key[0]
    check_char_count = 0
    for char in key:
        if char == check_char:
            check_char_count += 1
        score += ord(char)
    if score == 1337 and check_char_count == 3:
        return True
    return False

generate_key()


        
  

# References = [
# 'https://www.youtube.com/watch?v=IArt2Fgv644',
# 'https://www.geeksforgeeks.org/secrets-python-module-generate-secure-random-numbers/',
# ]
