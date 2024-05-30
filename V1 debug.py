#Number Guessing Game Objectives:
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


#from logo import art_logo
#import clear
import random

#print(art_logo)
#global and local variables?

#define games lives

EASY_GAMES_LIVES = 10
HARD_GAMES_LIVES = 5

#Step1: create a list of the numbers between 1 and 100
numbers = list(range(1,101))
#print(numbers)

#Step3:
#3.1 if the difference SelectedNumber > RandomNumber = return 'Too High'
#3.2 elif the difference SelectedNumber < RandomNumber = return 'Too Low'
#3.3 elif SelectedNumber == RandomNumber =return 'You win. '
#Problem: is their a need for a flag here? as While not Game_Over = True


guess = 0
while guess!= random_number:
    guess = int(input("Make a guess:  "))
    game_difficulty()

if guess > random_number:
    print('Too High')
elif guess < random_number:
    print ('Too Low')
elif guess == random_number:
    print('Winner! You guess right!')

#Step5: if the user selected easy only 10 opportunities. Only repeat the cycle 5 times if the 
        #elif the user selected hard only 5 opportunities. 
        #maybe using a for loop in range(5). and for loop in range(10) or with a counter

def game_difficulty():
    global EASY_GAMES_LIVES
    global HARD_GAMES_LIVES
    #while level_selection == 'easy' and easy_game_lives != 0: 
    if level_selection == 'easy':
      print(f"You have {EASY_GAMES_LIVES} attempts remaining to guess the number.")
      EASY_GAMES_LIVES -=1
      #print(easy_game_lives)
    #the games lives is 15
    else:
      print(f"You have {HARD_GAMES_LIVES} attempts remaining to guess the number")
      HARD_GAMES_LIVES -=1


#Step2: select a random number in that list. Print the selection for reference

random_number = int(random.choice(numbers))
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
print(f"Pss! the random number selected between 1 and 100 is: {random_number}")

#Step3: input a selection: easy of hard
level_selection = input("Choose a difficulty level. easy or hard?  ")

  #Step4: the user most take a guess

#Step6: define a function that allows the check if the input, in this case the number is too high or too low
#Problems: what reference do I am going to use to check if the number is to high or too low?
#The difference of the random number from the list and the selected number. This function must repeat itself.

    def check_the_number():
        if level_selection == 'easy' and EASY_GAMES_LIVES == 0:
          print('Out of attempts! you Lose!')
          game_over = True
        elif level_selection == 'hard' and HARD_GAMES_LIVES == 0:
          print('Out of attempts! you Lose!')


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


#Things different in my code:
#do not put inputs in the function that check answer. Inputs are guess, answer
#do not put a function for difficulty. level selection is in a variable not a
#function
#do not put global functions in ALL CAPS.
#do not declare global variable inside function. Just return it inside the function
#set difficulty should be before the make a guess and also before the choosing
#random number
#do not set the global variable guess = 0. I did not know where to put that while
#the check function answer goes on top of the difficulty levels



