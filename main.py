#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
r_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
list = []
for x in range(nr_letters):
    random_item = random.choice(letters)
    list.append(random_item)
for x2 in range(r_numbers):
    random_item2 = random.choice(numbers)
    list.append(random_item2)
for x3 in range(nr_symbols): 
    random_item3 = random.choice(symbols)
    list.append(random_item3)
word1 = ''.join(list)
print("\nPassword with characters:")
print(word1)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
list1 = []
for x in range(nr_letters):
    random_item = random.choice(letters)
    list1.append(random_item)
for x2 in range(r_numbers):
    random_item2 = random.choice(numbers)
    list1.append(random_item2)
for x3 in range(nr_symbols): 
    random_item3 = random.choice(symbols)
    list1.append(random_item3)
random.shuffle(list1)
shuffled_word = ''.join(list1)
print("\nPassword with characters randomised:")
print(shuffled_word)

#Another way of getting the password - easy way 
# for x in range(nr_letters):
#   random_item = random.choice(letters)
#   random1 = print(random_item, end='') 
# for x2 in range(r_numbers):
#   random_item2 = random.choice(numbers)
#   random2 = print(random_item2, end='')
# for x3 in range(nr_symbols): 
#   random_item3 = random.choice(symbols)
#   random3 = print(random_item3, end='')