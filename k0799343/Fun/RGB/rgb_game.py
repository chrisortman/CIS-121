start = """
You are in a dark room with 3 doors. 
On the left there is a red door. 
In the middle, a green one. 
The door on the right is blue.
Above the blue door, the number 
3 is printed in tiny red letters.
Choose a door.
"""

idk = "I don't know what that means."
ch1 = "Blank"
ch2 = "Blank"


print start

#color choice rgb
while ch1 != "red" and ch1 != "green" and ch1 != "blue":
    ch1 = raw_input("ch1>")

    if ch1 == "red":
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
                    print """
                    you get the key. As you're coming back, the tiger notices you passing and
                    attacks. After a short fight, the tiger kills you. THE END
                    """
                    
                elif "break" in ch3:
                    print "You break through the door. As you're leaving, you happen to notice the number '24' faintly printed on the door."
                
            else:
                print idk
            
       
    elif ch1 == "green":
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
        
    elif "blue" in ch1:
        print """
        You enter a mostly empty room. In the center there is a pedestal. On the top of the pedestal there appears to be
        a large padlock face with a number combination. You approach the pedestal. What do you do?
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
                    print "THE END"
                    
                else:
                    print "Nope"
                    
            else:
                print "Nope"
                
        else:
            print "Nope"
        
    else:
        print idk