from scene import Scene

class RedRoom(Scene):

    def enter(self):
        ch1 = "blank"
        ch2 = "blank"
        idk = "I don't know what that means."
        
  
        print """
        You enter through the red door and inside you find a wide hallway. 
        About halfway down the hall there is an anry tiger glaring at you.
        In front of you on a pedestal is a gun and a large raw steak. 
        You may choose one. 
        Gun or meat?"
        """
        
        while ch2 != "gun" and ch2 != "meat":
        #gun or meat
            ch2 = raw_input("ch2>")
            
            if "gun" in ch2:
                print "You kill the tiger and go through the door."
                
            elif "meat" in ch2:
                print """
                You throw the meat to the tiger and run to the door while it is distracted. 
                Once there however, you find that the door is locked. Turning back you see 
                a key on the floor by the door you entered through, but the tiger is almost
                done with the meat and will not be distracted for long. What do you do?
                """
                
                #key or break
                ch3 = raw_input("ch3>")
                
                if "key" in ch3:
                    print "you get the key"
                    
                elif "break" in ch3:
                    print "You break through the door"
                
            else:
                print idk
                
        return "main"