# from sys import argv

# script, text, surround = argv

def prancercise(text, surround):
    new = text.replace("_", " ")
    d = (("-")*10)
    return d+new.upper()+d
    
# prancercise(text, surround)
# transformed = prancercise("say_hi_to", "-")

# print "%s%s%s" % ((("-")*10), transformed, (("-")*10))