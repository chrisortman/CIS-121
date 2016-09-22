Class = "Blank"
choice = "Blank"

print "What type of person are you?"
print "1. Warrior"
print "2. Archer"
print "3. Mage"



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



#((((Start of Game))))

while Class != "Warrior" and Class != "Archer" and Class != "Mage":
    Class = raw_input("> ")
    if Class == "1" or Class == "Warrior":           #Warrior
        print "Grand, fan of hitting and kicking huh? Your stats are below."
        print ""
        print "Strength = 8"
        print "Dexterity = 4"
        print "Wisdom = 2"
    
        str = 8
        dex = 4
        wis = 2
        Class = "Warrior"

    elif Class == "2" or Class == "Archer":            #Archer
        print "Pleasent, love daggers and running huh? Your stats are below."
        print ""
        print "Strength = 2"
        print "Dexterity = 8"
        print "Wisdom = 4"
    
        str = 2
        dex = 8
        wis = 4
        Class = "Archer"

    elif Class == "3" or Class == "Mage":            #Mage
        print "Fantastic, enjoy power and magic huh? Your stats are below."
        print ""
        print "Strength = 2"
        print "Dexterity = 4"
        print "Wisdom = 8"
    
        str = 2
        dex = 4
        wis = 8
        Class = "Mage"

    else:
        print "That's not a class pal... Only use the numbers shown."
        
        
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
        
        
        
        
        
        