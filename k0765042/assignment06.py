
from sys import argv

script, text, surround = argv

def prancercise(text,surround):
    new = text.replace("_", " ")
    b = surround*10
    x = new.upper()
    print "%s%s%s" % (b,x,b)
    
prancercise(text,surround)