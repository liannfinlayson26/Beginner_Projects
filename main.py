from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print('Welcome to the secret auction program.')
bidders = {}
#modifications = []
continue_adding = True

#def name_size():
while continue_adding:
    key = input('What is your name?')
    value = float(input('What is your bid?'))
    bidders[key] = value
    question = input('Are there any bidders?')
    if question.lower() != 'yes':
        continue_adding = False
    else:
      clear()

max_value = max(bidders.values())
max_bidder = max(bidders, key=bidders.get)
print(f'The highster bidder is {max_bidder} with a bid of {max_value}')
# print(bidders)
#name_size()

# for names, sizes in list(bidders.items()):
#     size = bidders[names]
#     modifications.append(size) 
#     else:
#         name_size()
      
    

  
  
