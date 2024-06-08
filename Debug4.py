import random
from game_data import data
#Counter of points
points = 0
continue_playing = True

#Step 1: select random artist A
while continue_playing:
  random_artist1 = random.choice(data)
  name1 = random_artist1['name']
  description1 = random_artist1['description']
  country1 = random_artist1['country']
  follower_count1 = int(random_artist1['follower_count'])
  #print(random_artist)
  print(f"Compare A: {name1}, a {description1}, from {country1}")

  #Step 2: select random artist B

  random_artist2 = random.choice(data)
  name2 = random_artist2['name']
  description2 = random_artist2['description']
  country2 = random_artist2['country']
  follower_count2 = int(random_artist2['follower_count'])
  #print(random_artist)
  print(f"Compare B: {name2}, a {description2}, from {country2}")

#Step 3: Save correct answer
#getting the two options: capital letter or lower letter
  if follower_count1 > follower_count2:
    winner_choice = "A"
    print(winner_choice)
  else:
    winner_choice = random_artist2
    winner_choice = "B"
    print(winner_choice)

#Step 4: Input selection
  user_choice = input("Who has more followers? Type A or B: ")

#Step 5: Is choice correct?
  if winner_choice != user_choice:
    print(f"Sorry thats wrong! Final score: {points} ")
    continue_playing = False
  else:
    points += 1
    print(f"You are right! Current score: {points} ")
    #i could choose the winner choice A or B and replace it with the variable that stores the 



#Problems:
#1. how to keep playing the game and not get an infinite 
  #while loop

#2. how to replace the position B artist in the position A if the user got the right choice