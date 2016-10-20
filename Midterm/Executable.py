import time
from Kill import Death
from EchelonZero import echelon_zero
from EchelonOne import echelon_one
from EchelonTwo import echelon_two
from EchelonThree import echelon_three
from EchelonFour import echelon_four

class Cell(object):
    echelon_zero().enter()
    bit_zero = raw_input("> What do you do? ")
    if bit_zero == "GO_TO_SLEEP":
        Death().death()
    if bit_zero == "INSPECT_THE_CELL":
        echelon_one().enter()
        bit_one = raw_input("> What do you do? ")
        if bit_one == "KILL_HIM":
            echelon_two().enter()
            bit_two = raw_input("> What do you do? ")
        if bit_one == "ESCAPE":
            echelon_three().enter()
            bit_three = raw_input("> What do you do? ")
            if bit_three == "BREAK_DOOR":
                echelon_four().enter()
                print "> Your hero has become a legend by ending the cellmate"
                print "> threat. Now you can continue to build that legend"
                print "> through further gameplay and downloadable content."
            if bit_three == "CLIMB":
                print "> Your hero has become a legend by ending the cellmate"
                print "> threat. Now you can continue to build that legend"
                print "> through further gameplay and downloadable content."
            if bit_three == "KILL_HIM":
                print "> Your hero has become a legend by ending the cellmate"
                print "> threat. Now you can continue to build that legend"
                print "> through further gameplay and downloadable content."