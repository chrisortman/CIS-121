
####Imports
from sys import argv

####Variables
script, inputa, surround = argv

####Functions
def prancercise(inputa,surround):
    new = inputa.replace("_", " ")
    output = surround*10
    print output,
    print new.upper(),
    print output
    
####Main    
prancercise(inputa,surround)