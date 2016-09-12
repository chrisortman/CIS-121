"""
Assignment 4

8/36/16
"""
import sys #imports the system specfic parameters

base = int(sys.argv[1])   #takes the first argument and makes it a integer
height = int(sys.argv[2]) #takes the second argument and makes it a integer

###Math
area = base * height * .5 #Multiplies the base and height by 1/2 to get the area


####Main
print "The base of the triangle is:", base     #Prints the statement with the base
print "The height of the triangle is:", height #Prints the statement with the height
print "The Area of the triangle is:", area     #Prints the statement with the area calculated previously