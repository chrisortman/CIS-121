"""
Assignment 5

8/36/16
"""
####Import
import sys #imports the system specfic parameters

###ARG
base = int(sys.argv[1])   #takes the first argument and makes it a integer
height = int(sys.argv[2]) #takes the second argument and makes it a integer
count = 0
choiceq = "Would you like to change the height and base?"
####Math
area = base * height * .5 #Multiplies the base and height by 1/2 to get the area

####Functions
def output():
    print "The base of the triangle is:", base     #Prints the statement with the base
    print "The height of the triangle is:", height #Prints the statement with the height
    print "The Area of the triangle is:", area     #Prints the statement with the area calculated previously
    
def change_base_height():
    print "What would you like the new base to be? "
    base = int(raw_input())
    print "What would you like the new height to be? "
    height = int(raw_input())
    area = base * height * .5
    print "The base of the triangle is:", base     #Prints the statement with the base
    print "The height of the triangle is:", height #Prints the statement with the height
    print "The Area of the triangle is:", area     #Prints the statement with the area calculated previously

####Main
print choiceq
choicea = input()
if choicea == "y":
    if count == 0:
        output()
        count = count + 1
    else:
        Print "IMPOSSSIBLLE"
if choicea == "n":
    output()
    