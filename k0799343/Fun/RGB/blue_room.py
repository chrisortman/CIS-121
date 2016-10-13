from scene import Scene

class BlueRoom(Scene):

    def enter(self):
        ch1 = "blank"
        ch2 = "blank"
        idk = "I don't know what that means."
        


        print """
        You enter a mostly empty room. In the center there is a pedestal. On the top of the pedestal there appears to be
        a large padlock face with a number combination. You approach the pedestal. What number do you put?
        """
        ch6 = raw_input("ch6>")
        
        if '24' in ch6:
            print "The padlock clicks and the number '24' appears on the side of the pedestal. What do you do next?"
            
            ch6a = raw_input('ch6a>')
            
            if '43' in ch6a:
                print "The padlock clicks again and the number '43' appears next to the previous number. What do you do next?"
                
                ch6b = raw_input('ch6b>')
                
                if '3' in ch6b:
                    print """
                    The padlock clicks again and all 3 numbers appear on the pedestal, glowing for a second and then dissappearing. 
                    You hear the door at the far end of the room unlock and see it swing open. You stare at the door and slowly walk
                    towards it. You are free. 
                    """
                    return "finished"
                    
                else:
                    print "Nope"
                    
            else:
                print "Nope"
                
        else:
            print "Nope"
            
        return "main"