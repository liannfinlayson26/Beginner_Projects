import random
from game_data import data

#Present comparison A, select random comparison A from dictonaries 

def random_comparison(data):
  #randoms = random.sample(data, 2)
  #this probably needs to get consolidated in one. with two inputs 
  random_dicts = random.sample(data,2)
  for random_dict in random_dicts:
    print(f"Compare:  {random_dict('name')}, a {random_dict('description')}, from {random_dict('country')})
  #return random_data
print(random_comparison(data))


#ask who has more followers:
play_game = True
while play_game:
  user_answer = input("Who has more followers: Type 'A' or 'B' :")

#if answer is incorrect
  play_game = False
#if answer is correct
#problem: how to know where is the value of A if is in a random key? Call the function
  value_of_a = data[]
  if user_answer > 'follower_count'
  #this is a value inside a key
  play_game = True


  #present comparison A
  # random_comparison_a = random.choice(data)
  # value_name = random_comparison_a.get('name')
  # value_description = random_comparison.get('description')
  # value_country = random_comparison.get('country')

  # print(f"Compare A:  {value_name}, a {value_description}, from {value_country}") 

  #Present comparison B, select random comparison B from dictionaries

#   random_comparison_b = random.choice(data)
#   value_name_b = random_comparison_b.get('name')
#   value_description_b = random_comparison_b.get('description')
#   value_country_b = random_comparison_b.get('country')

#   print(f"Compare B: {value_name_b}, a {value_description_b}, from {value_country_b}") 

# random_comparison(data)