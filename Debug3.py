import random
from game_data import data

# random_artist1 = random.choice(data)
# name1 = random_artist1['name']
# description1 = random_artist1['description']
# country1 = random_artist1['country']
# follower_count1 = int(random_artist1['follower_count'])
# #print(random_artist)
# print(f"Compare A: {name1}, a {description1}, from {country1}")

# #Step 2: select random artist B
# random_artist2 = random.choice(data)
# name2 = random_artist2['name']
# description2 = random_artist2['description']
# country2 = random_artist2['country']
# follower_count2 = int(random_artist2['follower_count'])
# #print(random_artist)
# print(f"Compare B: {name2}, a {description2}, from {country2}")

def random_artist(a,b):
  random_artist= random.choice(data)
  name = random_artist1['name']
  description = random_artist['description']
  country = random_artist['country']
  follower_count = int(random_artist1['follower_count'])
  return (f"Compare {a=A} {name}, a {description}, from {country}")
  return (f"Compare {b=B} {name}, a {description}, from {country}")

random_artist(a,b)