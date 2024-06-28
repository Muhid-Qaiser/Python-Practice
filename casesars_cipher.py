from ceasars_cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

choice = 'yes'
checker = True


def caesar(text, shift, direction):
    end_text = ""

    if direction == "decode":
        shift *= -1

    for letter in text:
        if letter not in alphabet:
            end_text += letter
            continue
        position = (alphabet.index(letter) + shift) % 26
        end_text += alphabet[position]

    print(f"The {direction}d word is {end_text}.")


print(logo)

while checker:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    choice = input("Do you want to go again? Type 'yes' or 'no':\n").lower()

    if choice == 'no':
        checker = False

print("The End...\n")
