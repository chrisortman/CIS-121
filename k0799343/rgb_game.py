start = "Choose a door."
idk = "I don't know what that means."
ch1 = "Blank"
ch2 = "Blank"


print start

#color choice rgb
while ch1 != "red" and ch1 != "green" and ch1 != "blue":
    ch1 = raw_input("ch1>")

    if ch1 == "red":
        print "gun or meat?"
        
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
            
       
    elif ch1 == "green":
        print "What do you do?"
        
        ch4 = raw_input("ch4>")
        
        if "lazers" in ch4 or "lazer" in ch4:
            print "you slip and die."
            
        elif "panel" in ch4:
            print "You look at the panel"
            
            ch5 = raw_input("ch5>")
                
            if "num" in ch5:
                print "Correct"
                
                ch5a = raw_input("ch5a>")
                
                if "num" in ch5a:
                    print "Correct"
                    
                else:
                    print "Nope"
                
            else:
                print "Nope"
        
        
        
        
    else:
        print idk