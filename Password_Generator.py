# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = ""

# for i in range(0, nr_letters):
#   rad_letter = random.randint(0, len(letters))
#   password += letters[rad_letter]

# for i in range(0, nr_symbols):
#   rad_symbol = random.randint(0, len(symbols))
#   password += symbols[rad_symbol]

# for i in range(0, nr_numbers):
#   rad_number = random.randint(0, len(numbers))
#   password += numbers[rad_number]

# print(password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

temp_list = []
password = ""

for i in range(0, nr_letters):
    rad_letter = random.randint(0, len(letters))
    # temp_list.append(letters[rad_letter])
    temp_list += letters[rad_letter]

for i in range(0, nr_symbols):
    rad_symbol = random.randint(0, len(symbols))
    # temp_list.append(symbols[rad_symbol])
    temp_list += symbols[rad_symbol]

for i in range(0, nr_numbers):
    rad_number = random.randint(0, len(numbers))
    # temp_list.append(numbers[rad_number])
    temp_list += numbers[rad_number]

random.shuffle(temp_list)

for i in temp_list:
    password += i

print(password)
