from sys import argv
script, text, surround = argv

def prancercise(text,surround):
    new = text.replace("_", " ")
    b = surround*10
    print b,new.upper(),b
prancercise(text,surround)
