from logo import art_logo
#import clear
import random

EASY_GAME_LIVES = 10
HARD_GAME_LIVES = 5

def check_the_number(guess, random_number,turns):
  """Checks answer against guess. Returns the number of turns remaining"""
  if guess > random_number:
    print('Too High')
    return turns - 1 
  elif guess < random_number:
    print('Too Low')
    return turns - 1
  else:
    print(f'You got it! The answer was {random_number}')

#print(check_the_number())

def difficulty():
  level_selection = input("Choose a difficulty level. easy or hard?  ")
  if level_selection == 'easy':
    return EASY_GAME_LIVES
  else:
    return HARD_GAME_LIVES

def game():
  print(art_logo)
  print("Welcome to the Number Guessing Game!")
  print("I am thinking of a number between 1 and 100")
  numbers = list(range(1,101))
  random_number = int(random.choice(numbers))
  print(f"Pss! the random number selected between 1 and 100 is: {random_number}")
  
  turns = difficulty()

  guess = 0
  while guess != random_number:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess:  "))
    turns = check_the_number(guess, random_number, turns)
    if turns == 0:
      print("You've run out of guess, you lose.")
      return
    elif guess!= random_number:
      print("Guess again!")

game()