class Ship(object):

        def enter(self):
            print "You're stuck in the bottom of the ship and it's filling rapidly with water."
            print "Choose between: 1. a crowbar, 2. the trapdoor key, or 3. broccoli."
    
            action = raw_input("Choose number between 1-3> ")
    
            if action == "1":
                print "You bash the crowbar into the overhead trapdoor."
                print "You pry it open and a skeleton sees you and stabs you."
                print "You die.  You have two lives left."
                
                return 'water'
            
            elif action == "2":
                print "You find the key and unlock the trapdoor."
                print "Once you get out in the open, you run for it, promptly fall in a puddle and off the ship."
                print "There's a shark in the water.  You die.  You have two lives left."
               
                return 'water'
            
            elif action == "3":
                print "You find stale broccoli."
                print "You make friends with the shark through a window and he bashes it open.  (Sharks like broccoli)  You're free."
               
                return 'water'
            
            