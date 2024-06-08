import random
from game_data import data
from art import logo, vs
from replit import clear

def format_data(random_artist):
  """Takes the account data and return the printable format"""
  name = random_artist['name']
  description = random_artist['description']
  country = random_artist['country']
  return f"{name}, a {description}, from {country}"

def check_answer(user_choice, follower_count_1, follower_count_2):
  """Takes the user guess and follower counts and returns if they got it right"""
  if follower_count_1 > follower_count_2:
    if user_choice == 'a':
      return True
    #this is the same to write return guess == "a"
    else:
      return False
    #this is the same to write return guess == "b"
  
print(logo)

#Counter of points
points = 0
#Step 1: select random artist A and B. And make sure that they are not the same
continue_playing = True

#How to get that the second artist displayed becames the first one if the user guess correctly.
random_artist2 = random.choice(data)

while continue_playing:
  random_artist1 = random_artist2
  random_artist2 = random.choice(data)
  
  while random_artist1 == random_artist2:
    random_artist2 = random_choice(data)
  
  #calling the function
  print(f"Compare A: {format_data(random_artist1)} ")
  print(vs)
  print(f"Against B: {format_data(random_artist2)} ")
  
  
  # #Step 4: Input selection
  user_choice = input("Who has more followers? Type A or B: ").lower()
  
  # #Step 5: Is user choice correct?
  follower_count_1 = random_artist1['follower_count']
  follower_count_2 = random_artist2['follower_count']
  is_correct = check_answer(user_choice, follower_count_1, follower_count_2)

  #Clear the screen
  clear()
  print(logo)
  
  if is_correct:
    points += 1
    print(f"You are right! Current score: {points}")
  else:
    continue_playing = False
    print(f"Sorry thats wrong. Final score: {points}")
    