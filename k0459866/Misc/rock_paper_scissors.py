#WELCOME TO ROCK PAPER SCISSORS
#while True:
    
import random
import time

user = str(raw_input("Do you choose rock, paper, or scissors?\n"))

# rock = user = "rock" or "Rock"
# paper = user = "paper" or "Paper"
# scissors = user = "scissors" or "Scissors"
# error = user != rock or paper or scissors

foo = ['scissors', 'paper', 'rock']
comp = (random.choice(foo))
    
print "You chose %s." % user
time.sleep(0.5)
print "The computer chose %s." % comp
time.sleep(0.5)    
if (user == int):
    print "Numbers don't work here."

#rock
if (comp == "rock") and (user == "rock"):
    print "It's a tie."
elif (comp == "rock") and (user == "paper"):
    print "You win!"
elif (comp == "rock") and (user == "scissors"):
    print "You lose!"
#paper
elif (comp == "paper") and (user == "paper"):
    print "It's a tie."
elif (comp == "paper") and (user == "rock"):
    print "You lose!"
elif (comp == "paper") and (user == "scissors"):
    print "You win!"
#scissors
elif (comp == "scissors") and (user == "scissors"):
    print "It's a tie."
elif (comp == "scissors") and (user == "rock"):
    print "You win!"
elif (comp == "scissors") and (user == "paper"):
    print "You lose!"
#misc
elif (user == False):
    print "Make sure you chose something."
    
# if (comp == "rock"):
#     if (user == "rock"):
#         print "It's a tie."
#     elif (user == "paper"):
#         print "You win!"
#     elif (user == "scissors"):
#         print "You lose!"
        
# if (comp == "paper"):
#     if (user == "rock"):