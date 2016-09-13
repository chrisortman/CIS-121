from sys import argv

script, text, surround = argv

def prancercise(text, surround):
    new = text.replace("_", " ")
    d = surround * 10
    return d, new.upper(), d
#returns ('----------', 'SAY HI TO', '----------') ijnstead of (----------SAY HI TO----------)
prancercise(text, surround)
transformed = prancercise("say_hi_to", "-")

print transformed