from random import randrange

class Male:
    def __init__(self):
        self.pronoun = "M'Lord"
        self.address = "Sir"
        self.highaddress = "King"
        self.refer = "He"

class Female:
    def __init__(self):
        self.pronoun = "M'Lady"
        self.address = "Mam"
        self.highaddress = "Queen"
        self.refer = "She"

class GenderNeutral:
    def __init__(self):
        self.pronoun = "young heir"
        self.address = ""
        self.highaddress = "Ruler"
        self.refer = "They"
    
class Menu(object):

   def __init__(self):
       self.choices = []
       self.texts = []
       self.selected_value = None
       self.invalid_text = "That's not one of the choices, please use one of the numbers displayed."

   def add_choice(self, display_text, value):
       self.choices.append(value)
       self.texts.append(display_text)
   
   def current_weapon(self, weapon):
       self.current_weapon = weapon.selected_value

   def prompt(self, text):

       while self.selected_value is None:
           print text
           num = 1
           for display_text in self.texts:
               print "%d. %s" % (num, display_text)
               num = num + 1

           user_choice = int(raw_input("> "))

           if user_choice < 1 or user_choice > len(self.texts):
               print self.invalid_text
           else:
               self.selected_value = self.choices[user_choice - 1]
            
               
#((((Sparing Pit 1 / Weapon Select))))

def weapon():
    weapon = Menu()
    weapon.add_choice('Sword',1)
    weapon.add_choice('Shield',2)
    weapon.add_choice('Lance',3)
    weapon.add_choice('Mace',4)
    
    if startgame.selected_value == 1:
        print "Lord Maul: Good morning %s, glad you got here early. Maybe I'll go easy on you during training today." % player.pronoun
    else:
        print "Lord Maul: Sleep in early today again? You know the King never slept in during his sparring days. He alway wanted to try and put me in my place before he filled himself with mead."
    print ""
    print "Alright, lets get too it."
    print ""
    
    weapon.prompt("What do you want to work on today?")
    
    if weapon.selected_value == 1:
        print ""
    elif weapon.selected_value == 2:
        print ""
    elif weapon.selected_value == 3:
        print "" 
    elif weapon.selected_value == 4:
        thr1
        
    
#((((Sisters Room 1))))  
def sisroom_1():
    sisroom_1 = Menu()
    sisroom_1.add_choice('Sparing Pit',1)
    sisroom_1.add_choice('Sisters Room',2)
    sisroom_1.add_choice('Thrown Room',3)
    sisroom_1.add_choice('Dining Hall',4)
    
    sisroom_1.prompt("You get dressed and look out the window, where would you like to go?")
    
    if sisroom_1.selected_value == 1:
        weapon()
    elif sisroom_1.selected_value == 2:
        sisroom_1()
    elif sisroom_1.selected_value == 3:
        Thrownroom_1()
    elif sisroom_1.selected_value == 4:
        Dinehall_1()
        
        
def Thrownroom_1():
    thr1 = Menu()
    thr1.add_choice('Persuade to enter the room',1)
    thr1.add_choice('Go to Sparing Room',2)
    thr1.add_choice('Dining Hall',3)
    thr1.add_choice('Sisters Room',4)
    
    print "You walk down the hall to the thrown room but are stopped by two gaurds at the doors."
    print "Gaurd: Sorry %s, the Queen is in a negotiation right now with the Rockdawn Kingdom." % player.pronoun
    
    thr1.prompt("What do you say?")
    
    if thr1.selected_value == 1:
        print ""
    elif thr1.selected_value == 2:
        weapon()
    elif thr1.selected_value == 3:
        Dinehall_1() 
    elif thr1.selected_value == 4:
        sisroom_1() 
        
def Dinehall_1():
    weapon = Menu()
    weapon.add_choice('Sword',1)
    weapon.add_choice('Shield',2)
    weapon.add_choice('Lance',3)
    weapon.add_choice('Mace',4)
    
    if startgame.selected_value == 1:
        print "Lord Maul: Good morning %s, glad you got here early. Maybe I'll go easy on you during training today." % player.pronoun
    else:
        print "Sleep in early today again? You know the King never slept in during his sparring days. He alway wanted to try and put me in my place before he filled himself with mead."
    print "Alright, lets get too it."
    
    weapon.prompt("What do you want to work on today?")
    
    if weapon.selected_value == 1:
        print ""
    elif weapon.selected_value == 2:
        print ""
    elif weapon.selected_value == 3:
        print "" 
    elif weapon.selected_value == 4:
        print "" 
        
#def Startgame():

#((((Start of Game)))):

gender = Menu()
gender.add_choice('Male',Male)
gender.add_choice('Female',Female)
gender.add_choice('No preference',GenderNeutral)

print "What's your name?" 
ChaName = raw_input("> ")

gender.prompt("Gender?")

player = gender.selected_value()
print "---------------------------------------------------------------------------------------------------"
print "---------------------------------------------------------------------------------------------------"
print "---------------------------------------------------------------------------------------------------"
print "Welcome %s, you are a child of the royal family. Next in line for the thrown and become the next %s." % (ChaName, player.highaddress)
print "Right now your kingdom is in a mess and everyone is watching out for a knife in the back."
print "Your younger sister, Roth, is worried you may be in danger and could be on an assassins list along with the rest of your family."
print "You will have to make choices that influence your kingdom and watch your own neck for it may become a lot lighter if you don't."
print "Stay clam and keep your eyes peeled, watch out for danger and rule your kingdom how you want."
print "Do all that and you shall make a fine %s." % player.highaddress
print "---------------------------------------------------------------------------------------------------"
print "---------------------------------------------------------------------------------------------------"
print "---------------------------------------------------------------------------------------------------"
print " "

print "It's early in the day and the sun has just rose through the curtains."
print "Sir Saber(Your Butler): You know the sun only goes up once a day, might wanna see it before it's gone %s. Whenever you do decide to leave your bed don't forget that you have training today with Lord Maul. So please do get some breakfast and be on your way." % player.pronoun
print " "
print "(You shuffle out of bed and Sir Saber leaves the room)"
print " "

startgame = Menu()
startgame.add_choice('Sparing Pit',1)
startgame.add_choice('Sisters Room',2)
startgame.add_choice('Thrown Room',3)
startgame.add_choice('Dining Hall',4)

startgame.prompt("You get dressed and look out the window, where would you like to go?")

if startgame.selected_value == 1:
    weapon()
elif startgame.selected_value == 2:
    sisroom_1()
elif startgame.selected_value == 3:
    Thrownroom_1()
elif startgame.selected_value == 4:
    Dinehall_1()


