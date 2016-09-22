start = "Choose a door."
idk = "I don't know what that means."
ch1 = "Blank"

print start

#color choice rgb
while ch1 != "red" and ch1 != "green" and ch1 != "blue":
    ch1 = raw_input("ch1>")

    if ch1 == "red":
        print "gun or meat?"
        
        #gun or meat
        ch2 = raw_input("ch2>")
        
        if ch2 == "gun":
            print "You kill the tiger and go through the door."
            
        elif ch2 == "meat":
            print """
            You throw the meat to the tiger and run to the door while it is distracted. 
            Once there however, you find that the door is locked. Turning back you see 
            a key on the floor by the door you entered throuh, but the tiger is almost
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
        
    #how do i make it loop back to ch2?
    
    elif ch1 == "green":
        print "What do you do?"
        
        ch4 = raw_input("ch4>")
        
        if "lazers" in ch4:
            print "you slip and die."
            
        elif "panel" in ch4:
            print "You look at the panel"
            
        
        
        
        
        
        
    else:
        print idk