from prancercise import prancercise
from sys import argv

"""
try:
    
    prancercise(text, surround)
except ValueError:
    print "Please enter two arguements"
"""
if len(argv) == 3:
    _, text, surround = argv
    prancercise(text, surround)
    
else:
    print "Please enter two arguements"

    