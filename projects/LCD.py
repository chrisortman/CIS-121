def zero():
    print " __ "
    print "|  |"
    print "|__|"
    
def one():
    print "    "
    print "   |"
    print "   |"
    
def two():
    print " __"
    print " __|"
    print "|__ "

def three():
    print " __ "
    print " __|"
    print " __|"
    
def four():
    print "|_|"
    print "  |"
    
def five():
    print " __ "
    print "|__ "
    print " __|"

def six():
    print " __ "
    print "|__ "
    print "|__|"

def seven():
    print "  __"
    print "    |"
    print "    |"
    
def eight():
    print " __ "
    print "|__|"
    print "|__|"

def nine():
    print " __ "
    print "|__|"
    print "   |"


while True:
    x = raw_input("Type the number you would like printed: ")
    if x == '1':
        one()
    elif x == '2':
        two()
    elif x == '3':
        three()
    elif x == '4':
        four()
    elif x == '5':
        five()
    elif x == '6':
        six()
    elif x == '7':
        seven()
    elif x == '8':
        eight()
    elif x == '9':
        nine()
    elif x == '0':
        zero()
    else:
        print "Number not entered"
