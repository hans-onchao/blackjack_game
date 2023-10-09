import random

def get_choices():
  player_choice = input("enter a choice(rock, paper,scissors):")
  options =["rock","paper","scissors"]
  computer_choice = random.choice(options)
  choices ={"player":player_choice,"computer":computer_choice}
  return choices
  
def check_win(player,computer):
  print(f"you chose {player} ,computer chose {computer}")
  if player==computer:
    return "its a tie"
  elif player=="rock":
   if computer=="scissors":
      return "rock smarshes scissors, YOU WIN"
   else:
      return "paper covers rock, you lose"
  elif player=="paper":
   if computer=="paper":
      return "paper cover rock, YOU WIN"
   else:
      return "scissors cuts paper, you lose"
  elif player=="scissors":
   if computer=="paper":
      return "scissors cuts paper, YOU WIN"
   else:
      return "rock smashes scissors, you lose"
  
choices=get_choices()
result=check_win(choices["player"],choices["computer"])
print(result)
