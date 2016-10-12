########################################

# Programmed by J. Robert B.

import time
    
def enput(prompt):
    try:
        return input(prompt)
    except NameError:
        print "\"", input(prompt), "\"", " is not even a number, you fool."

# This program takes user input and echoes it.

echo_enabled = True

# It works by copying the input text and repeating it.

while echo_enabled == True:
    
    # The echo effect is defined by depth and rate.
    
    echo_depth = enput("What is the depth of the echo (in lines)? ")
    while echo_depth > 8 or echo_depth < 1:
        echo_depth = enput("Please enter a depth between 1 line and 8 lines. ")
    echo_rate = enput("What is the rate of the echo (in Hertz)? ")
    while echo_rate > 16 or echo_rate < 1 / 16:
        echo_rate = enput("Please enter a rate between 1/16 and 16 Hertz. ")
    # Depth is the number of lines that appear. Rate is the delay between lines.
    
    # The echo runs for five entries before asking for a new depth and rate.
    
    echo_mac = 5
    
    print "You may now use the Echo effect."
    
    while echo_mac > 0:
        echo_mac = echo_mac - 1

        if echo_depth == 8:
            echo_work = raw_input(".......  ")
            time.sleep(1 /echo_rate)
            print "...... ", echo_work, " ."
            time.sleep(1 /echo_rate)
            print "..... ", echo_work, " .."
            time.sleep(1 /echo_rate)
            print ".... ", echo_work, " ..."
            time.sleep(1 / echo_rate)
            print "... ", echo_work, " ...."
            time.sleep(1 / echo_rate)
            print ".. ", echo_work, " ....."
            time.sleep(1 / echo_rate)
            print ". ", echo_work, " ......"
            time.sleep(1 / echo_rate)
            print " ", echo_work, " ......."

        elif echo_depth == 7:
            echo_work = raw_input("......  ")
            time.sleep(1 / echo_rate)
            print "..... ", echo_work, " ."
            time.sleep(1 / echo_rate)
            print ".... ", echo_work, " .."
            time.sleep(1 / echo_rate)
            print "... ", echo_work, " ..."
            time.sleep(1 / echo_rate)
            print ".. ", echo_work, " ...."
            time.sleep(1 / echo_rate)
            print ". ", echo_work, " ....."
            time.sleep(1 / echo_rate)
            print " ", echo_work, " ......"

        elif echo_depth == 6:
            echo_work = raw_input(".....  ")
            time.sleep(1 / echo_rate)
            print ".... ", echo_work, " ."
            time.sleep(1 / echo_rate)
            print "... ", echo_work, " .."
            time.sleep(1 / echo_rate)
            print ".. ", echo_work, " ..."
            time.sleep(1 / echo_rate)
            print ". ", echo_work, " ...."
            time.sleep(1 / echo_rate)
            print " ", echo_work, " ....."

        elif echo_depth == 5:
            echo_work = raw_input("....  ")
            time.sleep(1 /  echo_rate)
            print "... ", echo_work, " ."
            time.sleep(1 / echo_rate)
            print ".. ", echo_work, " .."
            time.sleep(1 / echo_rate)
            print ". ", echo_work, " ..."
            time.sleep(1/ echo_rate)
            print " ", echo_work, " ...."

        elif echo_depth == 4:
            echo_work = raw_input("...  ")
            time.sleep(1 / echo_rate)
            print ".. ", echo_work, " ."
            time.sleep(1 / echo_rate)
            print ". ", echo_work, " .."
            time.sleep(1 / echo_rate)
            print " ", echo_work, " ..."

        elif echo_depth == 3:
            echo_work = raw_input("..  ")
            time.sleep(1 / echo_rate)
            print ". ", echo_work, " ."
            time.sleep(1 / echo_rate)
            print " ", echo_work, " .."

        elif echo_depth == 2:
            echo_work = raw_input(".  ")
            time.sleep(1 / echo_rate)
            print " ", echo_work, " ."
        
        else:
            echo_work = raw_input("  ")
            time.sleep(1 / echo_rate)
            print " "


# Programmed by J. Robert B.
# Copyleft FinalSynth


########################################