
####Imports
from sys import argv

####Variables
script, inputa, surround = argv

####Functions
def prancercise(inputa,surround):
    new = inputa.replace("_", " ")
    output = surround*10
    print str(output) + str(new.upper()) + str(output)
    
####Main    
prancercise(inputa,surround)