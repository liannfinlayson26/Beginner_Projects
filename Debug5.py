import random
from game_data import data

# Counter of points
points = 0
continue_playing = True

# Variables to store artist details
name1 = ""
description1 = ""
country1 = ""
follower_count1 = 0

# Function to generate random artist
def random_artist(label):
    random_artist = random.choice(data)
    name = random_artist['name']
    description = random_artist['description']
    country = random_artist['country']
    follower_count = int(random_artist['follower_count'])
    return name, description, country, follower_count

# Define the while loop
while continue_playing:
    # Step 1: select random artist A
    if not name1:  # If name1 is empty, it's the first round or a new game
        name1, description1, country1, follower_count1 = random_artist("A")
        print(f"Compare A: {name1}, a {description1}, from {country1}")

    # Step 2: select random artist B
    name2, description2, country2, follower_count2 = random_artist("B")
    print(f"Compare B: {name2}, a {description2}, from {country2}")

    # Save correct answer
    if follower_count1 > follower_count2:
        winner_choice = "A"
        winner_name, winner_description, winner_country, winner_follower_count = name1, description1, country1, follower_count1
    else:
        winner_choice = "B"
        winner_name, winner_description, winner_country, winner_follower_count = name2, description2, country2, follower_count2

    # Input selection
    user_choice = input("Who has more followers? Type A or B: ")

    # Is choice correct?
    if winner_choice != user_choice:
        print(f"Sorry, that's wrong! Final score: {points} ")
        continue_playing = False
    else:
        points += 1
        print(f"You are right! Current score: {points} ")
        print(f"The winner is: {winner_name}, a {winner_description}, from {winner_country} with {winner_follower_count} followers.")

    # Update artist A details for the next round
    if winner_choice == "A":
        name1, description1, country1, follower_count1 = name2, description2, country2, follower_count2
