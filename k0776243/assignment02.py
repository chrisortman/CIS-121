#calculate something :) for example "how many chickens?"
from sys import argv
#feline = input("How many cats do you have?")
# User is told to input number of cats and that is now the definition for feline
#canine = input("How many dogs do you have?")
# User is told to input number of dogs and that is now the definition for canine
script, feline, canine = argv
print "Marshall has", feline, "cats and", canine, "dogs"
# The string will be printed with the definitions of feline and canine in the appropriate places
print "One of each died.  Marshall is sad."
# This is a printed string
print "Here is the math:"
# This is also a printed string
print feline, "- 1"
# Feline is printed in a string
print canine, "- 1"
# Canine is printed in a string
alive_felines = int(feline) - 1
# We have a new term that equals feline - 1
alive_canines = int(canine) - 1
 # We have a new term that equals canine - 1
print "Now Marshall has only", alive_felines , "cats and", alive_canines, "dogs."
# This is a string with the new terms in the appropriate places
