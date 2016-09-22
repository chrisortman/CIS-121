Class = "Blank"
ClassSel = 0

print "What type of person are you?"
print "1. Warrior"
print "2. Archer"
print "3. Mage"

while Class != "Warrior" or  "Archer" or "Mage":
    ClassSel = raw_input("> ")
    if ClassSel == "1": #Warrior
        print "Grand, fan of hitting and kicking huh? Your stats are below. Well, lets get you into the world."
        print "Strength = 8"
        print "Dexterity = 4"
        print "Wisdom = 2"
    
        str = 8
        dex = 4
        wis = 2
        Class = "Warrior"

    elif ClassSel == "2": #Archer
        print "Pleasent, love daggers and running huh? Your stats are below. Well, lets get you into the world."
        print "Strength = 2"
        print "Dexterity = 8"
        print "Wisdom = 4"
    
        str = 2
        dex = 8
        wis = 4
        Class = "Archer"

    elif ClassSel == "3": #Mage
        print "Fantastic, enjoy power and magic huh? Your stats are below. Well, lets get you into the world."
        print "Strength = 2"
        print "Dexterity = 4"
        print "Wisdom = 8"
    
        str = 2
        dex = 4
        wis = 8
        Class = "Mage"

    else:
        print "That's not a class pal... Only use numbers."
  

print "So, whats your name good %s" % Class