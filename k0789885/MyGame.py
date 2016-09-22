Class = "Blank"

print "What type of person are you?"
print "1. Warrior"
print "2. Archer"
print "3. Mage"

def notvalid():
    print "That's not one of the choices, please use one of the numbers displayed."

def gameover():
    print "GAME OVER"
    quit()
    
def gochurch():
    print "1. Talk to the Father"
    print "2. Investigate gossip"
    print "3. Go to Alter"
    print "4. Leave"
    churchCh = ""
    while churchCh != 1 and churchCh != 2 and churchCh != 3 and churchCh != 4:
        churchCh = raw_input("> ")
        if churchCh == "1":
            FatherSpeak()
        elif churchCh == "2":
            if rumorhear != 1:
                if dex >= 8:
                    print "(You hear the nuns talking about the mysterious disappearens of multiple towns folk)"
                    print "(All victims have bite marks on there necks)"
                else:
                    rumor = "Speak of a murder case is going around"
            else:
                print "(You hear nothing else)"
        elif churchCh == "3":
            alter()
        elif churchCh == "4":
            arrivetown()
        else:
            notvalid()
            
def homes():
    print "1. Big home"
    print "2. Small home one"
    print "3. Small home two"
    print "4. Small home three"
    print "5. Leave"
    houseCh = ""
    while houseCh != 1 and houseCh != 2 and houseCh != 3 and houseCh != 4:
        houseCh = raw_input("> ")
        if houseCh == "1":
            homebig()
        elif houseCh == "2":
            home1()
        elif houseCh == "3":
            home2()
        elif houseCh == "4":
            home3()
        elif houseCh == "5":
            arrivetown()
        else:
            notvalid()

def mugman():
    print "He gets ready to fight."
    print "1. Attack man"
    print "2. Try to scare man"
    print "3. Take of mans cloak"
    print "4. Run away"
    fightVamp= ""
    while fightVamp != 1 and fightVamp != 2 and fightVamp != 3 and fightVamp != 4:
        fightVamp = raw_input("> ")
        if fightVamp == "1":
            if dex < 4:
                print "The man quickly bites your neck and drains you of all your blood. You died from blood loss."
                print ""
                gameover()
            else:
                if dex >= 8:
                    print "You quickly get behind the man and break his neck."
                elif str >= 8:
                    print "You knock the mans head clear off his shoulders."
                elif wis >= 8:
                    print "You set the man on fire, he turns to ash."
                else:
                    print "You have no good skills and die from lack of talent."
        elif fightVamp == "2":
            mugman()
        elif fightVamp == "3":
            print "You don't have any money."
        elif fightVamp == "4":
            if dex < 8:
                print "The man catches you and bites your neck, draining you of all your blood. You died from blood loss."
                print ""
                gameover()

            else:
                print "You get away safely."
        else:
            notvalid()
       

def cloaked_man():
    print "1. Ask the man how he is."
    print "2. Mug the man"
    print "3. Give the man money."
    print "4. Go back."
    choiceV = ""
    while choiceV != 1 and choiceV != 2 and choiceV != 3 and choiceV != 4:
        choiceV = raw_input("> ")
        if choiceV == "1":
            if Class == "Archer":
                VampireJob()
            else:
                print "(Silence)"
                cloaked_man()
        elif choiceV == "2":
            mugman()
        elif choiceV == "3":
            print "You don't have any money."
        elif choiceV == "4":
            bar()
        else:
            notvalid()       

def bar():
    print "There is a man in a dark cloak in the corner and the bartender is at the counter."
    BarCh = ""
    while BarCh != 1 and BarCh != 2 and BarCh != 3:
        print "What do you do?"
        print "1. Bartender"
        print "2. Maidens"
        print "3. Cloaked Man"
        print "4. Leave"
        BarCh = raw_input("> ")
        if BarCh == "1":
            bartender()
        elif BarCh == "2":
            maidens()
        elif BarCh == "3":
            print "(The air around him is grim and fills you with doubt.)"
            cloaked_man()
        elif BarCh == "4":
            arrivetown()
        else:
            notvalid()
            
def arrivetown():
    print "There is a bar, church, and a few homes. What would you like to go?"
    print "1. Bar"
    print "2. Church"
    print "3. Homes"
    print "4. Leave"
    choice = ""
    while choice != 1 and choice != 2 and choice != 3:
        choice = raw_input("> ")
        if choice == "1":
            print "You push the doors open and are greeted to a room of drunkards and maidens."
            bar()
        elif choice == "2":
            print "You walk into the church. The clergy seems unrested and the Father of the church is speaking to nuns."
            print "What do you do?"
            gochurch()
        elif choice == "3":
            print "(The houses consist of one large home and three small homes)"
            homes()
        elif choice == "4":
            print "You left the town to it's own fate, no need to get involved."
            print ""
            gameover()
        else:
            notvalid()
            
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
        print "Strength = 4"
        print "Dexterity = 2"
        print "Wisdom = 8"
    
        str = 4
        dex = 2
        wis = 8
        Class = "Mage"
        
    elif Class == "admin":

        ChaName = "Gage"
        str = 999
        dex = 999
        wis = 999
        
        print "Where to?"
        a = raw_input("> ")
        a()

    else:
        notvalid()        
        
print ""
print "So, whats your name good %s?" % Class
ChaName = raw_input("> ")

print "Good to meet you %s, let's get you into the world." % ChaName

print "You arrive at the small town of Rims Hide."
arrivetown()

        
        
        
        