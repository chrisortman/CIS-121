from scene import Scene

class GreenRoom(Scene):

    def enter(self):
        ch1 = "blank"
        ch2 = "blank"
        idk = "I don't know what that means."
        
        print """
        You enter a room with lots of lazers. It would be hard, but you might be able to squeeze your way through them. 
        Behind you is a panel with 3 switches. On the door opposite you, the number '43' is printed in big white numbers. 
        What do you do?
        """
        
        ch4 = raw_input("ch4>")
        
        if "lazers" in ch4 or "lazer" in ch4:
            print "you slip and die. THE END"
            
        elif "look" in ch4 or 'panel' in ch4:
            print "You look at the switches. The 1st switch is green, the 2nd switch is red, and the 3rd switch is blue. Which switch do you pull?"
            
            ch5 = raw_input("ch5>")
                
            if "red" in ch5:
                print "Correct. Some of the lazers turn off. Which one next?"
                
                ch5a = raw_input("ch5a>")
                
                if "green" in ch5a:
                    print "Correct. More of the lazers turn off. Now which switch?"
                    
                    ch5b = raw_input('ch5b>')
                    
                    if "blue" in ch5b:
                        print "Correct. You watch as the rest of the lazers slowly switch off. You leave the room."
                        
                        
                    else:
                        print "Nope"
                    
                else:
                    print "Nope"
                
            else:
                print "Nope"
        
        return "main"