Class = "Blank"
choice = "Blank"

class Warrior:
    def __init__(self):
        self.str = 8
        self.dex = 4
        self.wis = 2

    def greet(self):
        print "Grand, fan of hitting and kicking huh? Your stats are below."
        print ""
        print "Strength = %d" % self.str
        print "Dexterity = %d" % self.dex
        print "Wisdom = %d" % self.wis

class Archer:
    def __init__(self):
        self.str = 2
        self.dex = 8
        self.wis = 4

    def greet(self):
        print "Pleasent, love daggers and running huh? Your stats are below."
        print ""
        print "Strength = %d" % self.str
        print "Dexterity = %d" % self.dex
        print "Wisdom = %d" % self.wis

class Mage:
    def __init__(self):
        self.str = 2
        self.dex = 4
        self.wis = 8

    def greet(self):
        print "Fantastic, enjoy power and magic huh? Your stats are below."
        print ""
        print "Strength = %d" % self.str
        print "Dexterity = %d" % self.dex
        print "Wisdom = %d" % self.wis


def bar():
    print "You push the doors open and are greeted to a room of drunkards and maidens."
    print "There is a man in a dark cloak in the corner and the bartender is at the counter."
    while choice != 1 and choice != 2 and choice != 3:
        print "What do you do?"
        print "1. Bartender"
        print "2. Maidens"
        print "3. Cloaked Man"
        BarCh = raw_input("> ")
        if BarCh == "1":
            bartender()
        elif BarCh == "2":
            maidens()
        elif BarCh == "3":
            cloaked_man()
        else:
            print "That's not one of the choices, please use one of the numbers displayed."

class Menu(object):

    def __init__(self):
        self.choices = []
        self.texts = []
        self.selected_value = None
        self.invalid_text = "Invalid selection"

    def add_choice(self, display_text, value):
        self.choices.append(value)
        self.texts.append(display_text)


    def prompt(self, text):

        print "PROMPT %r" % self.selected_value

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



#((((Start of Game))))

archetype_menu = Menu()
archetype_menu.add_choice('Warrior',Warrior)
archetype_menu.add_choice('Archer',Archer)
archetype_menu.add_choice('Mage',Mage)
archetype_menu.invalid_text = "That's not a class pal... Only use the numbers shown."


archetype_menu.prompt("What type of person are you?")

player = archetype_menu.selected_value()

player.greet()

print ""
print "So, whats your name good %s?" % Class
ChaName = raw_input("> ")

print "Good to meet you %s, let's get you into the world." % ChaName

print "You arrive at the small town of Rims Hide. There is a bar, church, and a few homes. What would you like to visit?"
print "1. Bar"
print "2. Church"
print "3. Homes"
print "3. Leave"

while choice != 1 and choice != 2 and choice != 3:
    choice = raw_input("> ")
    if choice == "1":
        bar()
    elif choice == "2":
        church()
    elif choice == "3":
        homes()
    elif choice == "4":
        leave()
    else:
        print "That's not one of the choices, please use one of the numbers displayed."
        
        
        
        
        
        
        
        
        
        
        
        
