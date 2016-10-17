# Programmed by J. Robert B.

import time

# This program takes user input and echoes it.

echo_enabled = True

# It works by copying the input text and repeating it.

while echo_enabled == True:
    
    # The echo effect is defined by depth and rate.
    
    echo_depth = input("What is the depth of the echo? ")
    while echo_depth > 8 or echo_depth < 1:
        echo_depth = input("Please enter a depth between 1 line and 8 lines. ")
    echo_rate = input("What is the rate of the echo? ")
    while echo_rate > 16 or echo_rate < 1 / 16:
        echo_rate = input("Please enter a rate between 1/16 and 16 Hertz. ")
    
    # Depth is the number of lines that appear. Rate is the delay between lines.
    
    # The echo runs for five entries before asking for a new depth and rate.
    
    echo_mac = 5
    
    while echo_mac > 0:
        echo_mac = echo_mac - 1
        if echo_depth == 8:
            echo_work = raw_input(".......  ")
            time.sleep(echo_rate)
            print "...... ", echo_work, " ."
            time.sleep(echo_rate)
            print "..... ", echo_work, " .."
            time.sleep(echo_rate)
            print ".... ", echo_work, " ..."
            time.sleep(echo_rate)
            print "... ", echo_work, " ...."
            time.sleep(echo_rate)
            print ".. ", echo_work, " ....."
            time.sleep(echo_rate)
            print ". ", echo_work, " ......"
            time.sleep(echo_rate)
            print " ", echo_work, " .......", echo_mac
        elif echo_depth == 7:
            echo_work = raw_input("......  ")
            time.sleep(echo_rate)
            print "..... ", echo_work, " ."
            time.sleep(echo_rate)
            print ".... ", echo_work, " .."
            time.sleep(echo_rate)
            print "... ", echo_work, " ..."
            time.sleep(echo_rate)
            print ".. ", echo_work, " ...."
            time.sleep(echo_rate)
            print ". ", echo_work, " ....."
            time.sleep(echo_rate)
            print " ", echo_work, " ......", echo_mac

        elif echo_depth == 6:
            echo_work = raw_input(".....  ")
            time.sleep(echo_rate)
            print ".... ", echo_work, " ."
            time.sleep(echo_rate)
            print "... ", echo_work, " .."
            time.sleep(echo_rate)
            print ".. ", echo_work, " ..."
            time.sleep(echo_rate)
            print ". ", echo_work, " ...."
            time.sleep(echo_rate)
            print " ", echo_work, " .....", echo_mac

        elif echo_depth == 5:
            echo_work = raw_input("....  ")
            time.sleep(echo_rate)
            print "... ", echo_work, " ."
            time.sleep(echo_rate)
            print ".. ", echo_work, " .."
            time.sleep(echo_rate)
            print ". ", echo_work, " ..."
            time.sleep(echo_rate)
            print " ", echo_work, " ....", echo_mac

        elif echo_depth == 4:
            echo_work = raw_input("...  ")
            time.sleep(echo_rate)
            print ".. ", echo_work, " ."
            time.sleep(echo_rate)
            print ". ", echo_work, " .."
            time.sleep(echo_rate)
            print " ", echo_work, " ...", echo_mac

        elif echo_depth == 3:
            echo_work = raw_input("..  ")
            time.sleep(echo_rate)
            print ". ", echo_work, " ."
            time.sleep(echo_rate)
            print " ", echo_work, " ..", echo_mac

        elif echo_depth == 2:
            echo_work = raw_input(".  ")
            time.sleep(echo_rate)
            print " ", echo_work, " .", echo_mac
        else:
            print echo_work, echo_mac