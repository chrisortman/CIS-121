class Moltafari(object):
    
    def quit(self):
        return "quit()"
    
    def enter(self):
       print ""
       print "This is a volatile system were most worlds have a surface that is covered with flame and moltan rock." 
       answer = "yes"
       
       if answer == 'yes':
           print ""
           print "You sit down at the helm of the ship and throw levers forward as you jump into hyperspace"
           print "Your ship exits hyperspace arriving in Moltafari and directly infront of your ship lies a planet."
           print "Your second in command, Jack, walks up and asks you 'would you like us to scan it capatin?'"
           answer = raw_input("yes or no: ")
           # next system
           
           if answer == 'yes':
               print ""
               print "Your drone returns an hour later with data from the plantet. It appears that the surface is very volatile"
               print "with a active volcano spewing lava. But their is a small village away from the rivers of lava that seems fairly safe."
               print "Jack says 'Do you want us to land and try to make contact with the village capatin? Our ship could only last a hour'"
               answer = raw_input("yes or no: ")
               
               if answer == 'yes':
                   print ""
                   print "Very well captn' puttin the ship down"
                   print "Making a safe landing with the ashe from the volacano could prove a challange but Jack never dissapoints, you look out the window and"
                   print "spot the village, but you dont see any people moving about. 'Ready Captn?'"
                   answer = raw_input('yes or no: ')
                   
                   if answer == 'yes':
                       print ""
                       print "You and Jack exit the ship wearing your enviormental suits and start heading towards the village."
                       print "The huts are very rockish to protect from the harsh heat of the planet. You search around for a bit finding nothing but"
                       print "junk in the huts untill you enter one that has a living specimin inside. The organism apears the be a humanoid rock like"
                       print "nothing you have seen before. The rock creature turns and looks at you with an unmistakeable expression of fear on its"
                       print "face and starts to frantaclly gesture towards the door. In the background you hear a large rumble. 'I think its time to"
                       print "to go captn' Says Jack. When you and Jack exit the tent you see that the volcano in now rapidly sending balls of fire"
                       print "through the air. 'RUN!' Jack yells as you and him take off for the ship. Before you can reach the ship a giant fireball"
                       print "smashes through the hull. You and Jack are now stranded on this planet certin to die."
                       print ""
                       print ""
                       print "END GAME"
                       return quit()
                   if answer != 'yes':
                       print ""
                       print "'Was thinkging the same thing Captn', remember that we ony have fuel for 2 more jumps' "
                       print "The SS exploration takes off as it leaves the plant and goes on to the next sector."
                       print "You get to the next next sector and there is a planet in front of you."
                       print "Would you like to scan it?"
                       answer = raw_input("yes or no: ")
                       
                       if answer != 'yes':
                           print ""                                                    #THRID PLANET STARTS HERE
                           print "'Very well jumping to the next sector, we only have enough fuel to get home so we better find something here' says Jack."
                           print "You enter the last planet knowing that you have to find something here or you have failed your mission."
                           print "Jack approaces you, 'do you want to scan the last planet captn?"
                           answer2 = raw_input("yes or no: ")
                       
                       if answer2 == 'yes':
                           print ""
                           print "the scanner comes back a little while later wiht alarming news"
                           print "'it appears that not only is their life on thsi planet it is highly intelligent and they are sending warships towards us right now!' Jack syas frantaclly"
                           print "the exploration goes to jump out of the system but its too late. The alien fleet is already on them."
                           print "being a scouting ship the exporation doesnt stand a chance, all you can do is hope they have mercy as they close in."
                           print ""
                           print ""
                           print ""
                           print "GAME OVER"
                           return quit()
                           
                           
                       if answer2 != 'yes':
                           print "'Heading back to the capital as you wish captain.'"
                           print "your crew survives intact and well but you know they look at you with distain."
                           print "you prepare to report your failures when you get back, hey maybe they will show mercy."
                           print ""
                           print ""
                           print ""
                           print "GAME OVER"
                           return quit()
               
               if answer == 'yes':
                   print ""
                   print "You see that the planet in front of you in alike the one that you just visited from the scanner report"
                   print "after some further studying it looks like their is somekind of temple on the surface."
                   print "'Do you want to land captn?' asks Jack"
                   answer = raw_input("yes or no: ")
                   
                   if answer == 'yes':
                       print ""
                       print "The exploration sets down on the base of the planet near the temple and you and Jack get out to go exploring."
                       print "Do you want to go towards the temple or scout out the rockey terrian?"
                       answer1 = raw_input("Do you go towards the temple?   ")
                       
                   if answer != 'yes':
                       print ""                                                    #THRID PLANET STARTS HERE
                       print "'Very well jumping to the next sector, we only have enough fuel to get home so we better find something here' says Jack."
                       print "You enter the last planet knowing that you have to find something here or you have failed your mission."
                       print "Jack approaces you, 'do you want to scan the last planet captn?"
                       answer2 = raw_input("yes or no: ")
                       
                       if answer2 == 'yes':
                           print ""
                           print "the scanner comes back a little while later wiht alarming news"
                           print "'it appears that not only is their life on thsi planet it is highly intelligent and they are sending warships towards us right now!' Jack syas frantaclly"
                           print "the exploration goes to jump out of the system but its too late. The alien fleet is already on them."
                           print "being a scouting ship the exporation doesnt stand a chance, all you can do is hope they have mercy as they close in."
                           print ""
                           print ""
                           print ""
                           print "GAME OVER"
                           return quit()
                           
                           
                       if answer2 != 'yes':
                           print "'Heading back to the capital as you wish captain.'"
                           print "your crew survives intact and well but you know they look at you with distain."
                           print "you prepare to report your failures when you get back, hey maybe they will show mercy."
                           print ""
                           print ""
                           print ""
                           print "GAME OVER"
                           return quit()
                           
                       if answer1 == 'yes':                                         #NOT PART OF THIRD PLANET
                           print ""
                           print "you walk up to the the front door of the looming stone temple 'guess we should knock' jokes Jack"
                           print "you go up to the front of the large temple door and push on it. Supprisally it opens with ease."
                           print "through the door lies a room with 3 cups and a large engraving that reads 'drink and your safe passage will be certin.'"
                           print "'seems like one of them is the the correct one ay' jokes Jack"
                           print "let me go first if I die I know I will die for the capital plus the crew needs you to get back safely."
                           print "Which cup will Jack drink out of 1 2 or 3"
                           answer = raw_input("")
                           
                           if answer == '1':
                               print ""
                               print "Jack drinks from the cup the cup 'whew good guess captain I thought that I wasnt going to ma-' Jack falls over dead with the cup in his hand"
                               print "it is now up to you to carry on the mission"
                               print "guess another cup"
                               answer = raw_input("")
                               
                               if answer =='2':
                                   print ""
                                   print "you slowly drink the cup hoping that you guessesd correcly, then suddenly you feel an immensive pain swarm accross your body"
                                   print ""
                                   print ""
                                   print "You die GAME OVER"
                                   return quit()
                               if answer == '3': 
                                   print ""
                                   print "you drink from the cup and an ammzing feeling sweeps accross your body, you havnt felt this good in years."
                                   print "A secret door opens up in the wall and you enter, inside their is a massive pile of gold and diamonds"
                                   print "you have succed your mission!"
                                   print ""
                                   print ""
                                   print "YOU WIN!"
                                   return quit()
                               
                           if answer == '2':
                               print ""
                               print "Jack drinks from the cup the cup 'whew good guess captain I thought that I wasnt going to ma-' Jack falls over dead with the cup in his hand"
                               print "it is now up to you to carry on the mission"
                               print "guess another cup"
                               answer = raw_input("1 or 3: ")
                               
                               if answer == '1':
                                   print ""
                                   print "you slowly drink the cup hoping that you guessesd correcly, then suddenly you feel an immensive pain swarm accross your body"
                                   print ""
                                   print ""
                                   print "You die GAME OVER"
                                   return quit()
                               if answer == '3':
                                   print ""
                                   print "Jack drinks from the cup and and smiles, 'thats the best thing ive tasted in a while.'"
                                   print "A secret door opens up in the wall and you enter, inside their is a massive pile of gold and diamonds"
                                   print "you have succed your mission!"
                                   print ""
                                   print ""
                                   print "YOU WIN!"
                                   return quit()
                                  
                           if answer == '3':
                               print ""
                               print "Jack drinks from the cup and and smiles, 'thats the best thing ive tasted in a while.'"
                               print "A secret door opens up in the wall and you enter, inside their is a massive pile of gold and diamonds"
                               print "you have succeded your mission!"
                               print ""
                               print ""
                               print "YOU WIN!"
                               return quit()
                               
                               
                   if answer1 != 'yes':
                       print ""
                       print "you and Jack wonder around for a bit exploring the rocks and enjoying the nature"
                       print "suddenly a giant rock worm erupts out of the ground and mauls both of you"
                       print ""
                       print ""
                       print "GAME OVER"
                       return quit()
                   answer = raw_input("")
                   
               if answer != 'yes':
                   print ""
                   print "agreed captain remember we only have 2 fuel left to find something of value"
                   print "jumping to the next sector now"
                   print "you get to the next next sector and their their is a planet that is in front of you."
                   print "would you like to scan it?"
                   answer = raw_input("yes or no: ")
                   
                   if answer != 'yes':
                       print ""                                                    #THRID PLANET STARTS HERE
                       print "'Very well jumping to the next sector, we only have enough fuel to get home so we better find something here' says Jack."
                       print "You enter the last planet knowing that you have to find something here or you have failed your mission."
                       print "Jack approaces you, 'do you want to scan the last planet captn?"
                       answer2 = raw_input("yes or no: ")
                       
                       if answer2 == 'yes':
                           print ""
                           print "the scanner comes back a little while later wiht alarming news"
                           print "'it appears that not only is their life on thsi planet it is highly intelligent and they are sending warships towards us right now!' Jack syas frantaclly"
                           print "the exploration goes to jump out of the system but its too late. The alien fleet is already on them."
                           print "being a scouting ship the exporation doesnt stand a chance, all you can do is hope they have mercy as they close in."
                           print ""
                           print ""
                           print ""
                           print "GAME OVER"
                           return quit()
                           
                           
                       if answer2 != 'yes':
                           print "'Heading back to the capital as you wish captain.'"
                           print "your crew survives intact and well but you know they look at you with distain."
                           print "you prepare to report your failures when you get back, hey maybe they will show mercy."
                           print ""
                           print ""
                           print ""
                           print "GAME OVER"
                           return quit()
               
               if answer == 'yes':
                   print ""
                   print "you see that the planet in front of you in alike the one that you just visited from the scanner report"
                   print "after some further studying it looks like their is somekind of temple on the surface"
                   print "'do you want to land captn?' asks Jack"
                   answer = raw_input("yes or no: ")
                   
                   if answer != 'yes':
                       print ""
                       print "'very well jumping to the next sector we only have enough fuel to get home so we better find something here'"
                       print "you enter the last planet knowing that you have to find something here or you have failed yor mission."
                       print "Jack approaces you, 'do you want to scan the last planet captn?"
                       answer2 = raw_input("yes or no: ")
                   
                       if answer2 == 'yes':
                           print ""
                           print "the scanner comes back a little while later wiht alarming news"
                           print "'it appears that not only is their life on thsi planet it is highly intelligent and they are sending warships towards us right now!' Jack syas frantaclly"
                           print "the exploration goes to jump out of the system but its too late. The alien fleet is already on them."
                           print "being a scouting ship the exporation doesnt stand a chance, all you can do is hope they have mercy as they close in."
                           print ""
                           print ""
                           print ""
                           print "GAME OVER"
                           return quit()
                       if answer2 != 'yes':
                           print ""
                           print "'Heading back to the capital as you wish captain.'"
                           print "your crew survives intact and well but you know they look at you with distain."
                           print "you prepare to report your failures when you get back, hey maybe they will show mercy."
                           print ""
                           print ""
                           print ""
                           print "GAME OVER"
                           return quit()
                   
                   if answer == 'yes':
                       print ""
                       print "the exploration sets down on the base of the planet near the temple and you and Jack get out to go exploring"
                       print "'do you want to go towards the temple or scout out the rockey terrian?'"
                       answer = raw_input("Do you go towards the temple?   ")
                       
                       if answer == 'yes':
                           print ""
                           print "you walk up to the the front door of the looming stone temple 'guess we should knock' jokes Jack"
                           print "you go up to the front of the large temple door and push on it. Supprisally it opens with ease."
                           print "through the door lies a room with 3 cups and a large engraving that reads 'drink and your safe passage will be certin.'"
                           print "'seems like one of them is the the correct one ay' jokes Jack"
                           print "let me go first if I die I know I will die for the capital plus the crew needs you to get back safely."
                           print "Which cup will Jack drink out of 1 2 or 3"
                           answer = raw_input("")
                           
                           if answer == '1':
                               print ""
                               print "Jack drinks from the cup the cup 'whew good guess captain I thought that I wasnt going to ma-' Jack falls over dead with the cup in his hand"
                               print "it is now up to you to carry on the mission"
                               print "guess another cup"
                               answer = raw_input("2 or 3: ")
                               
                               if answer =='2':
                                   print ""
                                   print "you slowly drink the cup hoping that you guessesd correcly, then suddenly you feel an immensive pain swarm accross your body"
                                   print ""
                                   print ""
                                   print "You die GAME OVER"
                                   return quit()
                               if answer == '3': 
                                   print ""
                                   print "you drink from the cup and an ammzing feeling sweeps accross your body, you havnt felt this good in years."
                                   print "A secret door opens up in the wall and you enter, inside their is a massive pile of gold and diamonds"
                                   print "you have succed your mission!"
                                   print ""
                                   print ""
                                   print "YOU WIN!"
                                   return quit()
                               
                           if answer == '2':
                               print ""
                               print "Jack drinks from the cup the cup 'whew good guess captain I thought that I wasnt going to ma-' Jack falls over dead with the cup in his hand"
                               print "it is now up to you to carry on the mission"
                               print "guess another cup"
                               answer = raw_input("1 or 3: ")
                               
                               if answer == '1':
                                   print ""
                                   print "you slowly drink the cup hoping that you guessesd correcly, then suddenly you feel an immensive pain swarm accross your body"
                                   print ""
                                   print ""
                                   print "You die GAME OVER"
                                   return quit()
                               if answer == '3':
                                   print ""
                                   print "Jack drinks from the cup and and smiles, 'thats the best thing ive tasted in a while.'"
                                   print "A secret door opens up in the wall and you enter, inside their is a massive pile of gold and diamonds"
                                   print "you have succed your mission!"
                                   print ""
                                   print ""
                                   print "YOU WIN!"
                                   return quit()
                                  
                           if answer == '3':
                               print ""
                               print "Jack drinks from the cup and and smiles, 'thats the best thing ive tasted in a while.'"
                               print "A secret door opens up in the wall and you enter, inside their is a massive pile of gold and diamonds"
                               print "you have succeded your mission!"
                               print ""
                               print ""
                               print "YOU WIN!"
                               return quit()
                               
                               
                   if answer != 'yes':
                       print ""
                       print "you and Jack wonder around for a bit exploring the rocks and enjoying the nature"
                       print "suddenly a giant rock worm erupts out of the ground and mauls both of you"
                       print ""
                       print ""
                       print "GAME OVER"
                       return quit()
                   
           if answer != 'yes':
               print ""
               print "agreed captain remember we only have 2 fuel left to find something of value"
               print "jumping to the next sector now"
               
               print "you get to the next next sector and their their is a planet that is in front of you."
               print "Do you scan the planet?"
               answer = raw_input("yes or no: ")
               
               if answer == 'yes':
                   print ""
                   print "you see that the planet in front of you in alike the one that you just visited from the scanner report"
                   print "after some further studying it looks like their is somekind of temple on the surface"
                   print "'do you want to land captn?' asks Jack"
                   answer = raw_input("yes or no: ")
                   
                   if answer == 'yes':
                       print ""
                       print "the exploration sets down on the base of the planet near the temple and you and Jack get out to go exploring"
                       print "'do you want to go towards the temple or scout out the rockey terrian?'"
                       answer = raw_input("Do you go towards the temple?   ")
                       
                       if answer == 'yes':
                           print ""
                           print "you walk up to the the front door of the looming stone temple 'guess we should knock' jokes Jack"
                           print "you go up to the front of the large temple door and push on it. Supprisally it opens with ease."
                           print "through the door lies a room with 3 cups and a large engraving that reads 'drink and your safe passage will be certin.'"
                           print "'seems like one of them is the the correct one ay' jokes Jack"
                           print "let me go first if I die I know I will die for the capital plus the crew needs you to get back safely."
                           print "Which cup will Jack drink out of 1 2 or 3"
                           answer = raw_input("")
                           
                           if answer == '1':
                               print ""
                               print "Jack drinks from the cup the cup 'whew good guess captain I thought that I wasnt going to ma-' Jack falls over dead with the cup in his hand"
                               print "it is now up to you to carry on the mission"
                               print "guess another cup"
                               answer = raw_input("2 or 3: ")
                               
                               if answer =='2':
                                   print ""
                                   print "you slowly drink the cup hoping that you guessesd correcly, then suddenly you feel an immensive pain swarm accross your body"
                                   print ""
                                   print ""
                                   print "You die GAME OVER"
                                   return quit()
                               if answer == '3': 
                                   print ""
                                   print "you drink from the cup and an ammzing feeling sweeps accross your body, you havnt felt this good in years."
                                   print "A secret door opens up in the wall and you enter, inside their is a massive pile of gold and diamonds"
                                   print "you have succed your mission!"
                                   print ""
                                   print ""
                                   print "YOU WIN!"
                                   return quit()
                               
                           if answer == '2':
                               print ""
                               print "Jack drinks from the cup the cup 'whew good guess captain I thought that I wasnt going to ma-' Jack falls over dead with the cup in his hand"
                               print "it is now up to you to carry on the mission"
                               print "guess another cup"
                               answer = raw_input("1 or 3: ")
                               
                               if answer == '1':
                                   print ""
                                   print "you slowly drink the cup hoping that you guessesd correcly, then suddenly you feel an immensive pain swarm accross your body"
                                   print ""
                                   print ""
                                   print "You die GAME OVER"
                                   return quit()
                               if answer == '3':
                                   print ""
                                   print "Jack drinks from the cup and and smiles, 'thats the best thing ive tasted in a while.'"
                                   print "A secret door opens up in the wall and you enter, inside their is a massive pile of gold and diamonds"
                                   print "you have succed your mission!"
                                   print ""
                                   print ""
                                   print "YOU WIN!"
                                   return quit()
                                  
                           if answer == '3':
                               print ""
                               print "Jack drinks from the cup and and smiles, 'thats the best thing ive tasted in a while.'"
                               print "A secret door opens up in the wall and you enter, inside their is a massive pile of gold and diamonds"
                               print "you have succeded your mission!"
                               print ""
                               print ""
                               print "YOU WIN!"
                               return quit()
                               
                               
                   if answer != 'yes':
                       print ""
                       print "you and Jack wonder around for a bit exploring the rocks and enjoying the nature"
                       print "suddenly a giant rock worm erupts out of the ground and mauls both of you"
                       print ""
                       print ""
                       print "GAME OVER"
                       return quit()
    
               if answer != 'yes':
                   print ""
                   print "'very well jumping to the next sector we only have enough fuel to get home so we better find something here'"
                   print "you enter the last planet knowing that you have to find something here or you have failed yor mission."
                   print "Jack approaces you, 'do you want to scan the last planet captn?"
                   answer2 = raw_input("yes or no: ")
                   if answer2 == 'yes':
                           print ""
                           print "the scanner comes back a little while later wiht alarming news"
                           print "'it appears that not only is their life on thsi planet it is highly intelligent and they are sending warships towards us right now!' Jack syas frantaclly"
                           print "the exploration goes to jump out of the system but its too late. The alien fleet is already on them."
                           print "being a scouting ship the exporation doesnt stand a chance, all you can do is hope they have mercy as they close in."
                           print ""
                           print ""
                           print ""
                           print "GAME OVER"
                           return quit()
                   if answer2 != 'yes':
                           print ""
                           print "'Heading back to the capital as you wish captain.'"
                           print "your crew survives intact and well but you know they look at you with distain."
                           print "you prepare to report your failures when you get back, hey maybe they will show mercy."
                           print ""
                           print ""
                           print ""
                           print "GAME OVER"
                           return quit()