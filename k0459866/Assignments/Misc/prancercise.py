from sys import argv

# script, text, surround = argv

def prancercise(text, surround):
    new = text.replace("_", " ")
    return new.upper()
    
# prancercise(text, surround)
transformed = prancercise("say_hi_to", "-")

print "%s%s%s" % ((("-")*10), transformed, (("-")*10))