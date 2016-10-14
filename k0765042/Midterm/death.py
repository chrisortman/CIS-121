from scene import Scene
import random
lives = 2
class Finish(Scene):
    
    deaths = ["What are you, dead?", "You Have Run out of lives", "You suck at this"]

    def enter(self):
        if lives <= 0:
            print random.choice(deaths)
            print ("Would you like to play Again.")
            print ("Y or N")
            playagain = raw_input('>')
            if playagain == ("Y"):
                print "To bad so sad"
                return 'getting_to_know_everyone'
            elif playagain == ("N"):
                print("Good bye")
        else:
            print("You have one the Game")
            print("You were are last chance and you did not let us down")