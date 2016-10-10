name = raw_input("Enter your name: ")                # Enter your name
print "Welcome to the ship %s you are the captian of the SS exploration your mission is to find something of value and return it to the captial with your ship intact." % name

#def planetchoose():
print "Which system will you like to travel to frist?"
print "Moltafari    Aquari      Florari"
planet = raw_input("Choose a planet: ")
#return(planet)

#planetchoose()

if planet == 'Moltafari': 
   print "This is a volatile system were most worlds have a surface that is covered with flame and moltan rock." 
   print "Do you wish to continue?"
   print "yes or no?"
   answer = raw_input("")
   
   if answer == 'yes':
       print "You sit down at the helm of the ship and throw levers forward as you jump into hyperspace"
       print "Your ship exits hyperspace arriving in %s and directly infront of your ship lies a planet." % planet
       print "Your second in command, jack, walks up and asks you 'would you like us to scan it capatin?'"
       answer = raw_input("")
       # next system
       
       if answer == 'yes':
           print "your drone returns an hour later with data from the plantet. It appears that the surface is very volatile"
           print "with a active volcano spewing lava. But their is a small village away from the rivers of lava that seems fairly safe."
           print "Jack says 'Do you want us to land and try to make contact with the village capatin? Our ship could only last a hour'"
           answer = raw_input("")
       else:
           print "'Was thinkging the same thing Captn', remember that we ony have fuel for 2 more jumps' "
           print "The SS exploration takes off as it leaves the plant and goes on to the next sector"
           
           if answer == 'yes':
               print "very well captn' puttin the ship down"
               print "Making a safe landing with the ashe from the volacano could prove a challange but jack never dissapoints, you look out the window and"
               print "spot the village, but you dont see any people moving about. 'Ready Captn?'"
               answer = raw_input("")
           else:
               print "'Was thinkging the same thing Captn', remember that we ony have fuel for 2 more jumps' "
               print "The SS exploration takes off as it leaves the plant and goes on to the next sector"
               
        
               
               if answer == 'yes':
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
                   pass
               else:
                   print "'Was thinkging the same thing Captn', remember that we ony have fuel for 2 more jumps' "
                   print "The SS exploration takes off as it leaves the plant and goes on to the next sector"
                
   else:
        print "Which system will you like to travel to frist?"
        print "Moltafari    Aquari      Florari"
        planet = raw_input("Choose a planet: ")
       
      
                
                
                #   If they choose option 2 = This system is water based, most plants evolve around a water base ecosystem. Do you wish
                #   to continue?
                #   Option 1 = Yes, Option 2 = No
                
                #   If they choose option 3 = This is a land based system were most worlds mimic that on earth. Do you wish to continue?
                #   Option 1 = Yes, Option 2 = No
                
                # Moltafari path
                
                
                #       No = 
                #       next sector.
                
                #       [return to no outcome]
                
                #       
                
                #   No =  "very well captain jumping to the next sector we only have fuel to jump 2 more times then we have to head back 
                #          to the capital."
                
                #       The next planet that the exploration approaces is of similir readings as the first one.
                #       Jack, walks up and asks you "would you like us to scan it capatin?"
                
                #       Yes= The drone returns a short while later with data on the planet, the surface is dark and rocklike but their seems to be a large temple like structure.
                
                #       No= 
                
                # No = "very well captain jumping to the next sector we only have fuel to jump 2 more times then we have to head back 
                # to the capital."   
                
            