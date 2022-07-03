import random
import string

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                     'h', 'i', 'j', 'k', 'l', 'm', 'n',
                     'o', 'p', 'q', 'r', 's', 't', 'u',
                     'v', 'w', 'x', 'y', 'z']
uppercase_letters = []

# Converting letters to Uppercase & storing in a new Array
for letter in lowercase_letters:
    uppercase_letters.append(letter.upper())

# Variables are randomly set & change each time
random_uppercase_letter = uppercase_letters[random.randint(0, 25)]
random_lowercase_letter = lowercase_letters[random.randint(0, 25)]
random_number = random.randint(0, 9)
random_punctuation = string.punctuation[random.randint(0, len(string.punctuation) - 1)]

# All random characters are concatenated
concatenated_characters = random_punctuation + random_punctuation + random_uppercase_letter + random_uppercase_letter + random_lowercase_letter + random_lowercase_letter + str(random_number) + str(random_number)

# Characters are converted into an array
list_of_characters = list(concatenated_characters)
# Array is randomly shuffled
random.shuffle(list_of_characters)
# Array is joined together to make new password
final_password = ''.join(list_of_characters)

# Print out New Secure Password
print(final_password)

