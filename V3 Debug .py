alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(text1, cipher_shift, cipher_direction):
    text= ""
    if cipher_direction == 'decode':
        cipher_shift *= -1
    for letter in text1:
        new_position_text = alphabet.index(letter)
        new_position = new_position_text + cipher_shift
        text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(text1=text, cipher_shift=shift, cipher_direction=direction)