from itertools import cycle

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Encryption
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
my_list = []
alphabet_cycle = cycle(alphabet)
def encrypt(plain_text, shift_amount):
  for char in text:
    position = alphabet.index(char)
    position_2 = int(position)
    cypher_position = int(position_2 + shift)
    new_position = alphabet[cypher_position]
    my_list.append(new_position)
    # if cypher_position > 25:
    #     keep_running = next(alphabet_cycle)
    #     new_position_2 = alphabet.index(keep_running)
    #     new_cypher_position = int(new_position_2 + shift - 1)
    #     new_position_alpha = alphabet[new_cypher_position]
    #     my_list.append(new_position_alpha)
    # else:
    #   new_position = alphabet[cypher_position]
    #   my_list.append(new_position)

#Decryption
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
    plain_text =""
    for letter in cipher_text:
         new_position = alphabet.index(letter)
         old_position = new_position - shift_amount
         old_letter = alphabet[old_position]
         plain_text += old_letter
    print(f"The decoded text is {plain_text}")
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == 'encode'.lower():
    encrypt(plain_text=text, shift_amount=shift)
    result_string =''.join(my_list)
    print(f"The encoded text is {result_string}")
else:
    decrypt(cipher_text=text, shift_amount=shift)

  #print(position)
  #print(type(position))
#tendria que reemplazar los caracteres por los que se encuentren en la nueva posicion 
  #for position in range(len(alphabet)):
    #new_position = position + shift_amount
    #print(new_position)    

    #new_position = position + shift_amount
    #print(new_position)

    #print(position)
    #alphabet.index(text)
    ##new_position = alphabet.index(text) + shift
    #new_letter = alphabet[new_position]
    #print(new_letter)
  #range(len(text)):

  #for  letter in range(len(text),shift):   
    #print(text.index[shift])

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list


    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
