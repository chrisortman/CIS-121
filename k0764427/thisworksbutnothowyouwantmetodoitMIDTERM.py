name = raw_input("Enter your name: ")                # Enter your name
print "Welcome to the ship %s you are the captian of the SS exploration your mission is to find something of value and return it to the captial with your ship intact." % name

print "Which system will you like to travel to frist?"
print "Moltafari    Aquari      Florari"
planet = raw_input("Choose a planet: ")



if planet == "Moltafari":
    from moltafari import Moltafari
    
    planet = Moltafari()

    planet.enter()

if planet == "Aquari":
    from aquari import Aquari
    
    planet = Aquari()

    planet.enter()
    
if planet == "Florari":
    from florari import Florari   
    
    planet = Florari()

    planet.enter()

