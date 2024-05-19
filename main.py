rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choose_prs = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if choose_prs == 1:
  print(rock)
elif choose_prs == 0:
  print(paper)
elif choose_prs == 2:
  print(scissors)
else: 
  print("Blank")

print("The computer choose: ")
computer_choose = random.randint(0,2)
if computer_choose == 0:
    print(paper)
elif computer_choose == 1:
    print(rock)
else:
  print(scissors)

#paper = 0
#rock = 1
#scissors = 2

if choose_prs >= 3 or choose_prs < 0:
  print("You choose an incorrect number, you lose!")
elif choose_prs == 0 and computer_choose == 1:
  print("you win!")
elif choose_prs == 1 and computer_choose == 2:
  print("you win!")
elif choose_prs == 2 and computer_choose == 0:
  print("you win!")
elif choose_prs == computer_choose:
  print("its a tie")
else:
  print("you lose!")

# rock wins against scissors
# 0 = perder, 1 = ganar 
# list_1= [paper, rock, scissors]
# paper = ["ganar"]
# rock = ["ganar"]
# scissors = ["ganar"]
# paper_1 = "paper"
# rock_1 = "rock"
# scissors_1 = "scissors"

# game_1 = [paper_1, rock_1]
# game_2 = [rock_1, scissors_1]
# game_3 = [scissors_1, paper_1]
# combination = [game_1, game_2, game_3]

#esto imprime el simbolo de paper
# winner1 = combination[0][0]
# #rock
# loser1 = combination[0][1] 
# #rock
# winner2 = combination[1][0]
# #scissors
# loser2 = combination [1][1]
# #scissors
# winner3 = combination [2][0]
# #paper
# loser3 = combination[2][1]

# if game_1:
#   if choose_prs == winner1 and computer_choose == loser1:
#     print("you win")
# elif computer_choose == winner1 and choose_prs == loser1:
#     print("you lose")
# else:
#   print("its a tie")

# else:
#     if game_2:
#       if choose_prs == winner2 and computer_choose == loser2:
#         print("you win")
#       elif computer_choose == winner2 and choose_prs == loser2:
#         print("you lose")
#     else:
#       if game_3:
#         if choose_prs == winner3 and     computer_choose == loser3:
#           print("you win")
#       elif computer_choose == winner3 and         choose_prs == loser3:
#         print("you lose")
#       else:
#         print("its a tie!")


# print(winner2)
# print(winner3)


# if choose_prs == winner1:
#   print("You have won")
# elif choose_prs == loser1:
#   print("you lost")
# else:
#   print("Tie!")

# if winner:
#   print("You have won the game")
# else: 
#   print("you have lose the game")

# win1 = game_1[0]
# win2 = game_2[0]
# win3 = game_3[0]

# if game_1:
#   print(win1)
# elif game_2:
#   print(win2)
# else:
#   print(win3)


# print(list_1)
#ganar = list_1[0][1]
#print("ganar")

# paper wins against rock
# scissors wins against paper
