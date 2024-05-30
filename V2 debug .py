#Number Guessing Game Objectives:
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from logo import art_logo
#import clear
import random

print(art_logo)
#global and local variables?

#define games lives

easy_game_lives = 10
hard_game_lives = 5

#Step1: create a list of the numbers between 1 and 100
numbers = list(range(1,101))
#print(numbers)

#Step2: select a random number in that list. Print the selection for reference

random_number = int(random.choice(numbers))
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
print(f"Pss! the random number selected between 1 and 100 is: {random_number}")
  
  #Step3: input a selection: easy of hard
level_selection = input("Choose a difficulty level. easy or hard?  ")
  
  #Step4: the user most take a guess
while easy_game_lives  != 0 or hard_game_lives != 0 or guess == random_number: 
  guess = int(input("Make a guess:  "))

#Step5: if the user selected easy only 10 opportunities. Only repeat the cycle 5 times if the 
        #elif the user selected hard only 5 opportunities. 
        #maybe using a for loop in range(5). and for loop in range(10) or with a counter
  def game():
    global easy_game_lives
    global hard_game_lives
    if level_selection == 'easy':
      print(f"You have {easy_game_lives} attempts remaining to guess the number.")
      easy_game_lives -=1
      #print(easy_game_lives)
    #the games lives is 15
    else:
      print(f"You have {hard_game_lives} attempts remaining to guess the number")
      hard_game_lives -=1
  
  game()


#Step5: define a function that allows the check if the input, in this case the number is too high or too low
#Problems: what reference do I am going to use to check if the number is to high or too low?
#The difference of the random number from the list and the selected number. This function must repeat itself.
#3.1 if the difference SelectedNumber > RandomNumber = return 'Too High'
#3.2 elif the difference SelectedNumber < RandomNumber = return 'Too Low'
#3.3 elif SelectedNumber == RandomNumber =return 'You win. '
#Problem: is their a need for a flag here? as While not Game_Over = True

  def check_the_number():
    if guess > random_number:
      return 'Too High'
    elif guess < random_number:
      return 'Too Low'
    else:
      return 'Winner! You guess right!'
    
  print(check_the_number())
    

#when you start you have the full lives. As you progress you have
#less lives
#everytime you take a guess the number of lives decrease
#When does the game end? 
#If the player chooses easy and by the 5 time does not guess the number
#output: loser
#If the player chooses hard and by the 10 time does not guess the number
#output: loser
#If If the player guess correctly
#output: winner
