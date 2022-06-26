#This is a simple Rock, Paper, Scissors
# Game in Python
 
from random import*

prompt = "> "
options = ["rock", "paper", "scissors"]
state = "continue"
while(state == "continue"):
    answer = choice(options)
    User = input("Rock, Paper, Scissors!!(Type Quit to end game))\n %s" %(prompt))
    if(answer == User):
        print("You're so worthy!!")
    elif(User == "Quit" or User =="quit"):
        state = "Stop"
        print("\nGAME OVER\n")
    else:
        print("Looser!!")
 

        

