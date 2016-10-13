#lets me use argv
#from sys import argv

#assigns arguments to argv
#script, user_name = argv

#uses the arguments to say something
#print "Hi %s, I'm the %s script." % (user_name, script)

#does some math
math = 10*525343424+646436453534+4
#tells you the results of the math
print "MATH %d" % math

#does more math, says true or false
print "MATH2", 24/2<15

#prints a thing
print "###" 

#says to use the input entered here every time it says current_number
current_number=input("Enter current number:")

#adds the function with the rest of the code   
def print_100(arg1):

    #assigns variable sombra
    sombra= (100.0-current_number)/0.0038*3
    #prints sombra
    print "%d" % sombra,
    #prints context
    print "in minutes"

    #prints sombra/60
    print sombra/60,
    #prints context
    print "in hours"

    #prints sombra/60/24
    print sombra/60/24,
    #prints context
    print "in days"

    #more context
    print "until 100%"
    
    #using the argument
    print "%r" % (arg1)
    
#printing the function
print print_100(":)")